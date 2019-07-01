import time


class PID(object):

    def __init__(self, kp=1, ki=0, kd=0, ref=0, ilim=(-3, 3)):
        self.ref = ref
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self._i = 0
        self.ilim1 = ilim[0]
        self.ilim2 = ilim[1]
        self.primer_ciclo = True
        self.error_ans = 0
        self.last = 0

    def reset(self):
        self._i = 0
        self.primer_ciclo = True
        self.error_ans = 0

    def nueva_ref(self, valor):
        self.ref = valor
        self.primer_ciclo = True
        self._i = 0
        self.error_ans = 0

    def calcular(self, dato):
        now = time.ticks_ms()
        error = self.ref - dato
        dt = time.ticks_diff(now, self.last) / 1000

        p_error = error * self.kp

        if self.primer_ciclo:
            d_error = 0
            i_error = 0
            self.primer_ciclo = False
        else:
            if self.ilim1 < dato < self.ilim2:
                self._i += self.ki * (error + self.error_ans) * dt / 2
            else:
                self._i = 0

            d_error = self.kd * (error - self.error_ans) / dt
            i_error = self._i

        self.error_ans = error
        self.last = now

        return p_error + i_error + d_error
