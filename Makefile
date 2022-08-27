# Variables
I_TESTER = img_arach
TESTER = arachnida

V_SPIDER = $(PWD)/spider:/home/dev/spider
V_SCORPION = $(PWD)/scorpion:/home/dev/scorpion

all: dock
# Ejecuta contenedor creado
exec:
	@docker exec -it $(TESTER) bash

# Genera nuevo contenedor docker
dock: image
	@docker rm -fv $(TESTER) && docker run --name $(TESTER) -v $(V_SPIDER) -v $(V_SCORPION) -id $(I_TESTER)

# Genera imagen docker
image:
	@docker build -t $(I_TESTER) .

# Elimina contenedor 
clean:
	@docker rm -fv $(TESTER)

# Elimina imagen
fclean: clean
	@docker rmi $(I_TESTER)

# Elimina y crea una nueva imagen y un nuevo contenedor
re: fclean all 
