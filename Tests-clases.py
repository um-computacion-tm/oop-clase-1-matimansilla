import unittest
from Clases import Alumno, Materia, Profesor

class TestMateria (unittest.TestCase):
    
    def test_constructor(self):
        nombre='Redes'
        profesores=['Pablo','Carolina']
        redes=Materia(nombre,profesores)
        self.assertEqual(redes.__nombre__,'Redes')
        self.assertEqual(redes.__profesores__,['Pablo','Carolina'])
    
    def test_obtener_profesores(self):
        nombre='Redes'
        profesores=['Pablo','Carolina']
        redes=Materia(nombre,profesores)
        self.assertEqual(redes.obtener_profesores(),['Pablo','Carolina'])
    
    def test_cambiar_nombre(self):
        nombre='Redes'
        profesores=['Pablo','Carolina']
        redes=Materia(nombre,profesores)
        redes.cambiar_nombre('Calculo2')
        self.assertEqual(redes.__nombre__,'Calculo2')

class TestProfesor (unittest.TestCase):
     
     def test_profesor(self):
        profesores = Profesor("pablo", "titular", "6000")
        self.assertEqual(profesores.__nombre__, "pablo")
        self.assertEqual(profesores.__cargo__, "titular")
        self.assertEqual(profesores.__legajo__, "6000")

     def test_obtener_nomnbre(self):
        profesores = Profesor("pablo", "titular", "6000")
        self.assertEqual(profesores.obtener_nombre(), "pablo")

     def test_obtener_cargo(self):
        profesores = Profesor("pablo", "titular", "6000")
        self.assertEqual(profesores.obtener_cargo(), "titular")

     def test_obtener_legajo(self):
        profesores = Profesor("pablo", "titular", "6000")
        self.assertEqual(profesores.obtener_legajo(), "6000")

class TestAlumno (unittest.TestCase):
  
    def test_alumno(self):
        alumno = Alumno("Matias", "62131", "20", ".m.mansilla")
        self.assertEqual(alumno.__nombre__, "Matias")
        self.assertEqual(alumno.__legajo__, "62131")
        self.assertEqual(alumno.__edad__, "20")
        self.assertEqual(alumno.__mail__, ".m.mansilla") 

    def test_obtener_nombre(self):
        alumno = Alumno("Matias", "62131", "20", ".m.mansilla")
        self.assertEqual(alumno.obtener_nombre(), "Matias")

    def test_cambiar_mail(self):
        mail = ".m.mansilla"
        alumno = Alumno("Matias", "62131", "20", mail)
        alumno.cambiar_mail("i.milutin")
        self.assertEqual(alumno.__mail__, "i.milutin")






unittest.main()