import random
import time

# Introdução
print("🐾 Fuguinha do Crescimento 🐾")
print("Você é Simba! Corra, colecione ícones de aprendizado e siga em frente!\n")
time.sleep(1)

score = 0
steps = 0
icons = ["📚", "💡", "⭐"]

while steps < 10:
    action = input("Pressione Enter para correr...")  # qualquer tecla Enter
    steps += 1
    # Chance de pegar um ícone de aprendizado
    if random.random() < 0.6:
        icon = random.choice(icons)
        print(f"Você pegou um ícone de aprendizado {icon}!")
        score += 1
    else:
        print("Correu rápido, mas nada desta vez!")
    print(f"Passos: {steps} | Score: {score}\n")
    time.sleep(0.5)

print("🏁 Fim da corrida!")
print(f"Total de ícones coletados: {score}")
if score >= 7:
    print("💪 Incrível! Simba está crescendo rápido!")
elif score >= 4:
    print("😊 Bom! Continua correndo e aprendendo!")
else:
    print("⚡ Vamos mais rápido da próxima vez, Simba!")