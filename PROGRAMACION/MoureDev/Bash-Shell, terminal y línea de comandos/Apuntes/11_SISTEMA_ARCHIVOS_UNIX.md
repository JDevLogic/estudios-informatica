# GESTIÓN DE ARCHIVOS

## Sistema de archivos Unix

Los sistemas de archivos Unix están organizados por un único árbol jerárquico que empieza por `/`, llamado raíz.

### Directorios por defecto más típicos:

* `/` Raíz del sistema.
* `/home` Directorios personales de los usuarios.
* `/etc` Archivos de configuración del sistema.
* `/bin` Programas básicos.
* `/usr` Programas del usuario.
* `/var` Datos variables del sistema (registros, logs, colas...).
* `/tmp` Archivos temporales.

Puedes **explorar** un directorio sin encontrarte en él haciendo referencia a su ruta absoluta o relativa.

```
ls /
```