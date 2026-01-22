# KNS // COMMAND_NODE_NOC/SOC 🛡️

Este repositório contém a solução de **SOC/NOC Next-Gen** desenvolvida pela **KNS Consultoria**.  
O projeto foca em monitoramento proativo de infraestrutura para Provedores (ISPs) e empresas de tecnologia.

## 🚀 Diferenciais do Projeto

Diferente de dashboards convencionais, esta solução implementa uma lógica de **Segurança Ativa** e **UX Industrial**, projetada para ambientes críticos de operação 24/7.

* **Active Response Protocol (ARP)**: Mecanismo de resposta automática inspirado no conceito de *Dead Man’s Switch*. Caso um alerta crítico não seja validado pelo operador dentro de uma janela de 10 segundos, o sistema assume o controle e inicia ações de contenção.
* **Alerta Visual Absoluto**: Camada de sobreposição frontal (overlay) com sinalização crítica em vermelho intenso, eliminando riscos de falha humana por distração ou fadiga operacional.
* **Design Anti-Fadiga**: Temas Dark e Light cuidadosamente ajustados para operações contínuas, priorizando conforto visual e leitura rápida de métricas.
* **Integração Nativa**: Arquitetura desenvolvida para operar de forma transparente com Grafana e Zabbix, utilizando frames e painéis integrados.

## 🛠️ Tecnologias Utilizadas

* **Backend**: Python com Flask para gerenciamento de APIs de mitigação e automação de resposta.
* **Frontend**: HTML5, CSS3 (animações via keyframes) e JavaScript Vanilla.
* **Observabilidade**: Integração nativa com Grafana e Zabbix.
* **Ícones e Fontes**: FontAwesome e Google Fonts (Orbitron / Rajdhani).

## 🛡️ Active Response Protocol (ARP) em Ação

1. O sistema monitora continuamente anomalias de rede, como latência, packet loss e variações abruptas de tráfego.
2. Ao identificar um evento crítico ou comportamento suspeito, o **Active Response Protocol (ARP)** é acionado e inicia a contagem regressiva de 10 segundos.
3. Caso não haja intervenção humana dentro desse período, o **Alarme Crítico** é disparado, forçando a atenção do operador e priorizando a resposta imediata ao incidente.

## 👨‍💻 Desenvolvido por

**Kaleb Nunes dos Santos**  
*Consultor de Infraestrutura e Operações | KNS Consultoria*
