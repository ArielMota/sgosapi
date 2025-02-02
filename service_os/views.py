from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Empresa, Funcionario, OrdemServico
from .serializers import EmpresaSerializer, FuncionarioSerializer, OrdemServicoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    # Permissões
    def get_permissions(self):
        if self.action == 'create':
            # Permitir acesso público apenas para criação
            permission_classes = [AllowAny]
        else:
            # Requer autenticação para as outras ações
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]




class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]  # Exige que o usuário esteja autenticado

class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated]  # Exige que o usuário esteja autenticado
