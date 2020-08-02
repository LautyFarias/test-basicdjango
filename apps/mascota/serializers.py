from rest_framework.serializers import ModelSerializer
from apps.mascota.models import Mascota


class MascotaSerializer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombre', 'sexo', 'edad_aprox')
