from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
     """ 
     Cadastra um novo usuário no sistema e no banco de dados
     """

     if request.method == 'POST':
          nome = request.POST['nome']
          email = request.POST['email']
          senha = request.POST['password']
          senha2 = request.POST['password2']
          print(nome, email, senha, senha2)
          if campo_vazio(nome):
               messages.error(request, 'O campo nome não pode estar vazio')
               return redirect('cadastro')
          if campo_vazio(email):
               messages.error(request, 'O campo email não pode estar vazio')
               return redirect('cadastro')
          if senhas_diferentes(senha, senha2):
               messages.error(request, 'As senhas não são iguais')
               return redirect('cadastro')
          if User.objects.filter(email=email).exists():
               messages.error(request, 'Email já cadastrado')
               return redirect('cadastro')
          if User.objects.filter(username=nome).exists():
               messages.error(request, 'Usuário já cadastrado')
               return redirect('cadastro')

          user = User.objects.create_user(username=nome, email=email, password=senha)
          user.save()
          messages.success(request, 'Cadastro realizado com sucesso!')

          return  redirect('login')
     else:
          return render(request, 'usuarios/cadastro.html')


def login(request):
     """
     Realiza o login do usuário no sitema
     """

     if request.method == 'POST':
          email = request.POST['email']
          senha = request.POST['senha']
          if campo_vazio(email) or campo_vazio(senha):
               messages.error(request, 'Os campos Email e Senha não podem ficar vazios')
               return redirect('login')
          if User.objects.filter(email=email).exists():
               nome = User.objects.filter(email=email).values_list('username', flat=True).get()
               user = auth.authenticate(request, username=nome, password=senha)
               if user is not None:
                    auth.login(request, user)
                    return redirect('dashboard')
          else:
               messages.error(request, 'Email inválido')
     return render(request, 'usuarios/login.html')


def logout(request):
     """
     Realiza o logout do sistema
     """

     auth.logout(request)
     return redirect('index')


def dashboard(request):
     """
     Renderiza a página de dashboard caso o usuário esteja logado no sistema
     """

     if request.user.is_authenticated:
          id = request.user.id
          receitas = Receita.objects.order_by('data_receita').filter(pessoa=id)

          dados = {
               'receitas': receitas
          }

          return render(request, 'usuarios/dashboard.html', dados)
     else:
          return redirect('index')


def campo_vazio(campo):
     """
     Verifica se os campos de acesso e cadastros estão em branco
     """

     return not campo.strip()


def senhas_diferentes(senha, senha2):
     """
     Verifica se as senhas de cadastro são iguais
     """

     return senha != senha2


