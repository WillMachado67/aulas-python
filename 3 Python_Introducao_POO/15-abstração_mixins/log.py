# Abstração


from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')


    def log_error(self, msg):
        return self._log(f'Error: {msg}')


    def log_success(self, msg):
        return self._log(f'Succcess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            print('Salvando... ', msg_formatada)
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    


if __name__ == '__main__':
    # l = Log()
    lp = LogPrintMixin()
    lp.log_error('Agora foi')
    lp.log_success('qualquer coisa')
    lf = LogFileMixin()
    lf.log_error('Agora foi')
    lf.log_success('qualquer coisa')
