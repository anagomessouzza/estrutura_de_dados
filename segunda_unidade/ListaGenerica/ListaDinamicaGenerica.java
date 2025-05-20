package segunda_unidade.ListaGenerica;

public class ListaDinamicaGenerica <T> implements <Listavel> {
    private NoDuplo<T> ponteiroInicio;
    private NoDuplo<T> ponteiroFim;
    private int quantidade;
    private int tamanho;
    
    public ListaDinamicaGenerica (){
        this(10);
    }

    public ListaDinamicaGenerica (int tamanho){
        ponteiroInicio = null;
        ponteiroFim = null;
        quantidade = 0;
        tamanho = 0;
    }
    @Override
    public boolean estaCheia(){
        return quantidade == tamanho;
    }

    @Override
    public boolean estaVazia(){
        return quantidade == 0;
    }

    @Override
	public String imprimir() {
		String resultado = "[";
		NoDuplo<T> ponteiroAuxiliar = ponteiroInicio;		
		for (int i = 0; i < quantidade; i++) {
		if (i == quantidade-1) {
				resultado += ponteiroAuxiliar.getDado();
			} else {
				resultado += ponteiroAuxiliar.getDado() + ",";
			}
			ponteiroAuxiliar = ponteiroAuxiliar.getProximo();
		}
		return resultado + "]";
	}
}

// comecei a ficar com a mente cansada na aula, terminar depois 