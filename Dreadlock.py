from random import randint
class Dreadlock:

  ##Construtor da classe;
  def __init__(self):

    ##Variaveis
    self.processos = 0;
    self.recursos = 0;    


  ## Metodo inicializador
  def run(self):
    ##Entrada de dados de processo e recursos;
    self.entradaDeDados();
    ## Entrada de dados de quantos recursos terão disponiveis
    self.recursosExistentes();

    ## Enquanto res for "S" executamos a adição de pedidos de novos recursos.
    res = 'S'
    while res == 'S':
      # Re processa a matriz
      self.processamentoMatriz();
      ## Pergunta se deseja continua
      res = str(input("Deseja adicionar mais recursos aos processos? (S/N): ")).strip().upper()[0];
      
  def recursosExistentes(self):
    self.vtRecursosExistentes = [0] * self.recursos;

    for recExistentes in range(0, len(self.vtRecursosExistentes)):
      self.vtRecursosExistentes[recExistentes] = int(input("Digite o total de Recursos existentes na Posição({}): ".format(recExistentes)));

  def entradaDeDados(self):

    #pegando os valores dos inputs de processo e recursos
    totalProcess = int(input("Digite o total de processos: "));
    totalRecursos = int(input("Digite o total de recursos: "));
    ## setando os novos valores
    self.processos = totalProcess;
    self.recursos = totalRecursos;

    ## matriz simples
    self.vtRecursosAlocados = [0] * self.recursos;
    self.vtQueroAlocar = [0] * self.recursos;
    

  def processamentoMatriz(self):

    #iniciado a matriz com colunas
    self.mtzRequisicoes = [];
    self.mtzAlocacaoCorrente = [];
    ## criando a matriz com os processos e recursos solicitados;
    for mtzReq in range(0, self.processos):
      self.mtzRequisicoes.append([0] * self.recursos);
    for mtzAloc in range(0, self.processos):
      self.mtzAlocacaoCorrente.append([0] * self.recursos);

    ## preenchendo a matriz com os dados
    for processos in range(0, self.processos):
      for recursos in range(0, self.recursos):
        self.mtzRequisicoes[processos][recursos] = int(input("Digite o total de recurso a ser alocado no Processo({}) e no Recurso({}): ".format(processos, recursos)));
    self.matrizRequisicoes();

  def matrizRequisicoes(self):
    qtdeRecursoParaAlocar = 0;

    for recursoAtual in range(0, self.recursos):
      qtdeRecursoParaAlocar = 0;

      for processoAtual in range(0, self.processos):
        qtdeRecursoParaAlocar += self.mtzRequisicoes[processoAtual][recursoAtual];

      self.vtQueroAlocar[recursoAtual] = self.vtRecursosAlocados[recursoAtual] + qtdeRecursoParaAlocar;
      if self.vtRecursosExistentes[recursoAtual] >= self.vtQueroAlocar[recursoAtual]:
        # "encher" a mtzAlocacaoCorrente
			  # atualizar vetor vtRecursosAlocados
        self.vtRecursosAlocados[recursoAtual] += qtdeRecursoParaAlocar;
        print('Você poderá alocar os recursos ({}) mas o total que poderá armazena é ({}).\n'.format(self.vtRecursosAlocados[recursoAtual], self.vtRecursosExistentes[recursoAtual]));
      else:
        print('Não é possível alocar mais recursos');
        print('Você deseja alocar ({}) que será superior ao permitido que é ({}) no total.\n'.format(qtdeRecursoParaAlocar, self.vtRecursosExistentes[recursoAtual]));