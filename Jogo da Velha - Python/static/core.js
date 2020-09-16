function Jogada(cel_id,campo_id,jogador) {
    if (document.getElementById(cel_id).value == 0){ 
    document.getElementById(cel_id).value = jogador
        if (jogador == 1){
        document.getElementById(campo_id).innerHTML = "O"
        }
        else{
        document.getElementById(campo_id).innerHTML = "X"    
        }

    }
}