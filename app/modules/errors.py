# -*- coding: utf-8 -*-


class BaseModuleException(Exception):
    '''Bu bizim kendi hata sınıfımız'''
    def __init__(self, msg):
        super(BaseModuleException, self).__init__(msg)


class AlreadyExistsException(BaseModuleException):
    '''Herhangi bir kayıt zaten varsa, bu hata dönecek'''
    def __init__(self, msg):
        super(AlreadyExistsException, self).__init__(msg)


class WrongArgumentException(BaseModuleException):
    '''Argümanlar eksik, fazla ya da hatalı gönderildiyse,
    bu hata fırlatılacak'''
    def __init__(self, msg):
        super(WrongArgumentException, self).__init__(msg)


class NotFoundException(BaseModuleException):
    '''Bir şey bulunamadıysa bu hata fırlatılacak.'''
    def __init__(self, msg):
        super(NotFoundException, self).__init__(msg)


class NotAllowedException(BaseModuleException):
    '''İzinsiz işlerde bu fırlayacak.'''
    def __init__(self, msg):
        super(NotAllowedException, self).__init__(msg)
