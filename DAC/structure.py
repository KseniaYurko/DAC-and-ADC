try:
    исполяем какой-то код
except Exception as e:
    обработка исключения
else:
    код, который будет исполнен в случае, когда не возникает исключения
finally:
    код, который гарантированно будет исполнен последним (всегда исполняется)