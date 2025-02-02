from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Empresa, Funcionario, OrdemServico

class EmpresaSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)  # Recebe o email para criação do usuário
    password = serializers.CharField(write_only=True)  # Recebe a senha de forma segura

    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco', 'telefone', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # A senha será apenas escrita e não retornada

    def validate_email(self, value):
        # Verifica se o email já existe no sistema
        if User.objects.filter(email=value).exists():
            raise ValidationError("empresa com este email já existe.")
        return value

    def create(self, validated_data):
        # Criação do usuário
        user = User.objects.create_user(
            username=validated_data['email'],  # Usando o email como username
            email=validated_data['email'],
            password=validated_data['password']  # A senha é automaticamente hashed
        )

        # Criação da empresa
        empresa = Empresa.objects.create(
            user=user,  # Vinculando o usuário à empresa
            nome=validated_data['nome'],
            cnpj=validated_data['cnpj'],
            endereco=validated_data['endereco'],
            telefone=validated_data['telefone']
        )

        return empresa

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = '__all__'
