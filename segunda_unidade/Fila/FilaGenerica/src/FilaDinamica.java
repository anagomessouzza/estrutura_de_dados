package Fila.FilaGenerica.src;

import java.util.NoSuchElementException;

public class FilaDinamica<T> implements Enfileiravel{
    private ponteiroInicio;
    private ponteiroFim;
    private tamanho;
    private quantidade;


    public FilaDinamicaGenerica(int tamanho) {
		quantidade = 0;
		this.tamanho = tamanho;
		ponteiroInicio = null;
		ponteiroFim = null;
	}

    public FilaDinamicaGenerica(){
        this(10);
    }

    @Override
    void enfileirarInicio(T dado){
        throw new UnsupportedOperationException("Operação não suportada!");

    }
    @Override
    void desenfileirarFim(T dado){
        throw new UnsupportedOperationException("Operação não suportada!");

    }
    @Override
    public T tras();{ 
        throw new UnsupportedOperationException("Operação não suportada!");
    }

    void enfileirarFim(T dado);

    @Override
    public T frent(){
        if (estaVazia()){
            throw new NoSuchElementException("Fila vazia!");
        }
        T dadoInício = ponteiroInicio.getDado();
        return dadoInício;
    }
    /*
     * 
     */
    @Override
    public void atualizarInicio(T dado){
        if(estaVazia()){
            throw new NoSuchElementException("Fila vazia!");
        }
        ponteiroInicio.setDado(dado);
    }
    @Override
    public void atualizarFim(T dado){
        if(estaVazia()){
            throw new NoSuchElementException("Fila vazia!");
        }
        ponteiroFim.setDado(dado);
    }
    @Override
    T desenfileirarInicio(){
        if (estaVazia()){
            throw new NoSuchElementException("Fila está vazia");
        }
        T dadoInício = ponteiroInicio.getDado();
        ponteiroInicio = ponteiroInicio.getProximo();
        ponteiroInicio.setAnterior(null); // importante para desenfileirar
        quantidade --;
        return dadoInício;

        public void enfileirarFim(T dado){
            if (estaCheia()){
            throw new NoSuchElementException("Fila está vazia");
        }
            NodoDuplo<T> novoNodo = new NodoDuplo(dado);
            novoNodo.setAnterior(ponteiroFim);
            if (!estaVazia())
                ponteiroFim.setProximo(novoNodo);
            else
                ponteiroFim = novoNodo;
            quantidade ++;
        }

    public boolean estaCheia(){
        return quantidade == tamanho;
    }

    String imprimirDeFrentePraTras(){
        String retorno = "[";
        NodoDuplo<T> aux = ponteiroInicio;
        for (int i=0; i<quantidade;
        i ++){
            aux.getDado();
            if(i != quantidade -1);
            aux =aux.getProximo();
        }
        return retorno + "]";
    }





    
}
