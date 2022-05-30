segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

qtd_horas_dia = 24
qtd_minutos_hora = 60
qtd_segudos_minuto = 60

qtd_segundos_dia = (qtd_horas_dia * qtd_minutos_hora * qtd_segudos_minuto) # Quantidade de segundos por dia
dias = total_segs // qtd_segundos_dia                                      # Divide pela quantidade de dias
resto_dias = total_segs % qtd_segundos_dia                                 

qtd_segundos_hora = (qtd_minutos_hora * qtd_segudos_minuto)                # Quantidade de segundos por hora
resto_horas = resto_dias % qtd_segundos_hora

minutos = resto_horas // qtd_segudos_minuto
segundos = resto_horas % qtd_segudos_minuto

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e", segundos, "segundos.")