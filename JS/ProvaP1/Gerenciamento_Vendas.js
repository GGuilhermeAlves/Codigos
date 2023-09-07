const prompt = require("prompt-sync")();

class Produto {
    constructor(id, nome, preco, quantidade) {
        this.id = id;
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }
}

let obterId = 0;
const produtos = [];
const vendas = [];

function adicionarProduto(nome, preco, quantidade) {
    if (nome.trim() === "") {
        return "Nome inválido. O nome do produto não pode ser vazio.";
    }

    if (isNaN(preco) || preco <= 0 || isNaN(quantidade) || quantidade <= 0) {
        return "Valores inválidos. O preço e a quantidade devem ser números positivos maiores que zero.";
    }

    if (/^\d+$/.test(nome)) {
        return "Nome inválido. O nome do produto não pode ser composto apenas por números.";
    }

    const novoProduto = new Produto(obterId + 1, nome, preco, quantidade);
    produtos.push(novoProduto);
    obterId++;
    return `Produto "${nome}" adicionado com sucesso! ID do produto: ${novoProduto.id}`;
}

function atualizarProduto(id, novoNome, novoPreco, novaQuantidade) {
    if (novoNome.trim() === "") {
        return "Nome inválido. O nome do produto não pode ser vazio.";
    }

    if (
        isNaN(novoPreco) ||
        novoPreco <= 0 ||
        isNaN(novaQuantidade) ||
        novaQuantidade < 0
    ) {
        return "Valores inválidos. O novo preço deve ser um número positivo maior que zero e a nova quantidade deve ser um número não negativo.";
    }

    if (/^\d+$/.test(novoNome)) {
        return "Nome inválido. O nome do produto não pode ser composto apenas por números.";
    }

    const produto = encontrarProdutoPorId(id);

    if (produto) {
        produto.nome = novoNome;
        produto.preco = novoPreco;
        produto.quantidade = novaQuantidade;
        return `Produto com ID ${id} atualizado com sucesso!`;
    } else {
        return `Não foi possível atualizar, pois o produto com ID ${id} não está cadastrado no sistema!`;
    }
}

function removerProduto(id) {
    const produto = encontrarProdutoPorId(id);

    if (produto) {
        produto.quantidade = 0;
        return `Estoque do produto "${produto.nome}" com ID ${id} removido com sucesso!`;
    } else {
        return `Não foi possível remover o estoque, pois o produto com ID ${id} não está cadastrado no sistema!`;
    }
}

function venderProduto(id, quantidade) {
    const produtoVendido = encontrarProdutoPorId(id);

    if (produtoVendido) {
        if (isNaN(quantidade) || quantidade <= 0) {
            return "Valor inválido. A quantidade deve ser um número positivo maior que zero.";
        }

        if (produtoVendido.quantidade >= quantidade) {
            produtoVendido.quantidade -= quantidade;
            const valorTotal = quantidade * produtoVendido.preco;
            registrarVenda(produtoVendido.nome, quantidade, valorTotal);
            return `Você comprou ${quantidade} unidades de ${produtoVendido.nome
                } (ID: ${id}) por R$${valorTotal.toFixed(2)}`;
        } else {
            return `Não é possível vender ${quantidade} unidades do produto com ID ${id}, pois só temos ${produtoVendido.quantidade} em estoque`;
        }
    } else {
        return `Não é possível vender ${quantidade} unidades do produto com ID ${id}, pois este produto não está cadastrado`;
    }
}

function encontrarProdutoPorId(id) {
    return produtos.find((produto) => produto.id === id);
}

function registrarVenda(nome, quantidade, valorTotal) {
    vendas.push({ nome, quantidade, valorTotal });
}

function gerarBoletoVendas() {
    let totalVendas = 0;
    let boleto = "===== BOLETO DE VENDAS =====\n";

    for (const venda of vendas) {
        boleto += `Produto: ${venda.nome}, Quantidade: ${venda.quantidade
            }, Valor Total: R$${venda.valorTotal.toFixed(2)}\n`;
        totalVendas += venda.valorTotal;
    }

    boleto += `Total: R$${totalVendas.toFixed(2)}\n`;
    boleto += "=============================";
    return boleto;
}

function relatorioEstoque(tipoRelatorio) {
    let produtosRelatorio;

    switch (tipoRelatorio) {
        case 1:
            produtosRelatorio = produtos;
            break;
        case 2:
            produtosRelatorio = produtos.filter((produto) => produto.quantidade > 0);
            break;
        case 3:
            produtosRelatorio = produtos.filter(
                (produto) => produto.quantidade === 0
            );
            break;
        default:
            produtosRelatorio = produtos;
            break;
    }

    const relatorio = produtosRelatorio.map((produto) => {
        return `ID: ${produto.id}, Nome: ${produto.nome
            }, Preço: R$${produto.preco.toFixed(2)}, Quantidade: ${produto.quantidade}`;
    });

    return relatorio;
}

function exibirMenu() {
    console.log("Sistema de Vendas e Gerenciamento de Estoque!");
    console.log("========= MENU =========");
    console.log("[1] Adicionar Produto");
    console.log("[2] Atualizar Produto");
    console.log("[3] Remover Produto");
    console.log("[4] Vender Produto");
    console.log("[5] Relatório de Estoque");
    console.log("[0] Sair");
    console.log("========================");
}

function exibirMenuRelatorio() {
    console.log("========= RELATÓRIO =========");
    console.log("[1] Todos os Produtos");
    console.log("[2] Produtos em Estoque");
    console.log("[3] Produtos sem Estoque");
    console.log("[0] Voltar ao Menu Principal");
    console.log("============================");
}

function executarAcao(opcao) {
    do {
        switch (opcao) {
            case "1":
                adicionarProdutoMenu();
                break;
            case "2":
                atualizarProdutoMenu();
                break;
            case "3":
                removerProdutoMenu();
                break;
            case "4":
                venderProdutoMenu();
                console.log(gerarBoletoVendas());
                break;
            case "5":
                console.clear();
                exibirMenuRelatorio();
                const tipoRelatorio = prompt("Digite o tipo de relatório desejado:");
                exibirRelatorio(tipoRelatorio);
                break;
            case "0":
                console.clear();
                console.log("Saindo do sistema...");
                return;
            default:
                console.clear();
                console.log("Opção inválida. Por favor, tente novamente.");
                break;
        }

        exibirMenu();
        opcao = prompt("Digite a opção desejada:");
    } while (opcao !== "0");
}

function adicionarProdutoMenu() {
    let continuarAdicionar = true;

    while (continuarAdicionar) {
        const nome = prompt("Digite o nome do produto (ou 0 para voltar ao menu):");

        if (nome === "0") {
            continuarAdicionar = false;
            console.clear();
            break;
        }

        const preco = parseFloat(prompt("Digite o preço do produto (Ex: 000.00):"));
        const quantidade = parseInt(prompt("Digite a quantidade do produto:"));

        if (isNaN(preco) || isNaN(quantidade)) {
            console.log("Valor inválido. Por favor, tente novamente.");
        } else {
            console.log(adicionarProduto(nome, preco, quantidade));
        }
    }
}

function atualizarProdutoMenu() {
    let continuarAtualizar = true;

    while (continuarAtualizar) {
        const idAtualizar = parseInt(
            prompt(
                "Digite o ID do produto a ser atualizado (ou 0 para voltar ao menu):"
            )
        );

        if (idAtualizar === 0) {
            continuarAtualizar = false;
            console.clear();
            break;
        }

        const novoNome = prompt("Digite o novo nome do produto:");
        const novoPreco = parseFloat(
            prompt("Digite o novo preço do produto (Ex: 000.00):")
        );
        const novaQuantidade = parseInt(
            prompt("Digite a nova quantidade do produto:")
        );

        if (isNaN(novoPreco) || isNaN(novaQuantidade)) {
            console.log("Valor inválido. Por favor, tente novamente.");
        } else {
            console.log(
                atualizarProduto(idAtualizar, novoNome, novoPreco, novaQuantidade)
            );
        }
    }
}

function removerProdutoMenu() {
    let continuarRemover = true;

    while (continuarRemover) {
        const idRemover = parseInt(
            prompt(
                "Digite o ID do produto a ser removido (ou 0 para voltar ao menu):"
            )
        );

        if (idRemover === 0) {
            continuarRemover = false;
            console.clear();
            break;
        }

        console.log(removerProduto(idRemover));
    }
}

function venderProdutoMenu() {
    let continuarVendas = true;

    while (continuarVendas) {
        const idVender = parseInt(
            prompt("Digite o ID do produto a ser vendido (ou 0 para voltar ao menu):")
        );

        if (idVender === 0) {
            continuarVendas = false;
            console.clear();
            break;
        }

        const quantidadeVender = parseInt(
            prompt("Digite a quantidade a ser vendida:")
        );

        if (isNaN(quantidadeVender)) {
            console.log("Valor inválido. Por favor, tente novamente.");
        } else {
            console.log(venderProduto(idVender, quantidadeVender));
        }
    }
}

function exibirRelatorio(tipoRelatorio) {
    switch (tipoRelatorio) {
        case "1":
            console.clear();
            console.log("Relatório: Todos os Produtos");
            console.log(relatorioEstoque(1));
            break;
        case "2":
            console.clear();
            console.log("Relatório: Produtos em Estoque");
            console.log(relatorioEstoque(2));
            break;
        case "3":
            console.clear();
            console.log("Relatório: Produtos sem Estoque");
            console.log(relatorioEstoque(3));
            break;
        case "0":
            console.clear();
            exibirMenu();
            const opcao = prompt("Digite a opção desejada:");
            executarAcao(opcao);
            break;
        default:
            console.clear();
            console.log("Opção inválida. Por favor, tente novamente.");
            exibirMenuRelatorio();
            const novaOpcao = prompt("Digite o tipo de relatório desejado:");
            exibirRelatorio(novaOpcao);
            break;
    }
}

console.clear();
exibirMenu();
const opcaoMenu = prompt("Digite a opção desejada:");
executarAcao(opcaoMenu);
