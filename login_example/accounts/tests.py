from django.test import TestCase
from .models import CustomUser
from .forms import RegistroForm
from django.urls import reverse

class UsuarioTests(TestCase):
    
    # Verificar que el ORM de Django guarde correctamente un usuario anfitrion
    def test_creacion_usuario_anfitrion(self):
        # 1. ARRANGE (preparar datos de prueba)
        correo_prueba = 'host@gmail.com'
        password_prueba = "liston12345"
        
        # 2. ACT (ejecutar la funcion a probar)
        usuario = CustomUser.objects.create_user(
            username='host_test',
            email = correo_prueba, 
            password=password_prueba,
            is_host = True
        )
        
        # 3. ASSERT (comprobar que el resultado es el esperado)
        self.assertEqual(usuario.email, correo_prueba)
        self.assertTrue(usuario.is_host)
        self.assertFalse(usuario.is_renter)
        

class RegistroFormTests(TestCase):
    
    # Verificar que el formulario de registro no permita registrar usuarios sin email
    def test_formulario_rechaza_sin_correo(self):
        # 1. ARRANGE (preparar lo que escribiria el usuario)
        datos_formulario = {
            'username': 'moneda',
            'is_renter': True
        }
        
        # 2. ACT (le pasamos estos datos al formulario)
        form = RegistroForm(data=datos_formulario)
        
        # 3. ASSERT (comprobar que el formulario detecte el error)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

class RegistroViewTests(TestCase):
    
    # Verificar que la pagina de registro de usuario cargue correctamente
    def test_pagina_registro_carga_correctamente(self):
        
        # 1. ARRANGE y 2. ACT (usamos el navegador de pruebas para entrar a la URL de registro)
        url = reverse('registro')
        response = self.client.get(url)
        
        # 3. ASSERT (comprobar que el codigo de status de la peticion http sea 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/registro.html')