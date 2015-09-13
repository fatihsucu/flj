# -*- coding: utf-8 -*-


class BaseException(Exception):
    '''Bu bizim kendi hata sınıfımız'''
    def __init__(self, message, code=30):
        super(BaseException, self).__init__(message)
        self.message = message
        self.code = code

    def __json__(self):
        return {
            "type": self.__class__.__name__,
            "message": self.message,
            "code": self.code}

    def __str__(self):
        return "{}: code: {}, message: {}".format(
            self.__class__.__name__,
            self.code,
            self.message)


class AlreadyExistsException(BaseException):
    '''Herhangi bir kayıt zaten varsa, bu hata dönecek'''
    def __init__(self, message, code=31):
        super(AlreadyExistsException, self).__init__(message, code)


class WrongArgumentException(BaseException):
    '''Argümanlar eksik, fazla ya da hatalı gönderildiyse,
    bu hata fırlatılacak'''
    def __init__(self, message, code=32):
        super(WrongArgumentException, self).__init__(message)


class NotFoundException(BaseException):
    '''Bir şey bulunamadıysa bu hata fırlatılacak.'''
    def __init__(self, message, code=33):
        super(NotFoundException, self).__init__(message)


class NotAllowedException(BaseException):
    '''İzinsiz işlerde bu fırlayacak.'''
    def __init__(self, message, code=34):
        super(NotAllowedException, self).__init__(message)
