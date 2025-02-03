from rest_framework import permissions

class EmpresaCustomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            # POST é público (qualquer usuário pode criar empresa)
            return True
        elif request.method == "GET":
            # GET (listar empresas) só pode ser feito por administradores autenticados
            if view.action == 'list':
                # Administradores podem listar todas as empresas
                return request.user and request.user.is_authenticated and request.user.is_staff
            elif view.action == 'retrieve':
                # Usuário logado pode ver sua própria empresa
                return request.user and request.user.is_authenticated
        else:
            # Outras ações exigem autenticação e permissões de admin
            return request.user and request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Permite que o admin veja todas as empresas ou que o dono da empresa veja a sua
        return (
            request.user and request.user.is_authenticated and (
                request.user.is_staff or obj.user == request.user
            )
        )



class IsEmpresaOrReadOnly(permissions.BasePermission):
    """
    Permite acesso total apenas para a empresa dona do objeto. Outros podem apenas ler.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user, 'empresa') and obj.empresa.user == request.user


class IsFuncionarioAssignedOrReadOnly(permissions.BasePermission):
    """
    Permite que funcionários visualizem suas OS, mas não editem outras.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user, 'funcionario') and obj.funcionario and obj.funcionario.user == request.user
