import re

s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"

reg = r'[+]?[7][\d][\d]+'
print(re.findall(reg, s))
# Ответ
# ['+74994564578','74994564578']
