import sys
import re

html_input = "c:/Users/PC/Desktop/site ebook novo/index.html"
html_output = "c:/Users/PC/Desktop/site ebook novo/design-system-completo.html"

with open(html_input, "r", encoding="utf-8") as f:
    content = f.read()

style_match = re.search(r'(<style>.*?</style>)', content, re.DOTALL)
if style_match:
    style_block = style_match.group(1)
else:
    print("Erro: não encontrou <style>")
    sys.exit(1)

html_docs = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Design System - Tráfego Pago Premium Dark</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">

{style_block}

<style>
/* ════════════════════════════════════════════════════
   ESTILOS EXCLUSIVOS DA DOCUMENTAÇÃO DO DESIGN SYSTEM
   ════════════════════════════════════════════════════ */
.ds-container {{ max-width: 1200px; margin: 0 auto; padding: 120px 20px; font-family: var(--font-body); }}
.ds-section {{ margin-bottom: 80px; padding-bottom: 56px; border-bottom: 1px solid var(--color-border-default); }}
.ds-title {{ font-family: var(--font-display); font-size: var(--text-32); font-weight: var(--w-bold); margin-bottom: 40px; color: var(--color-text-primary); }}
.ds-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 32px; }}
.ds-swatch {{ border-radius: var(--r-lg); overflow: hidden; border: 1px solid var(--color-border-default); margin-bottom: 16px; box-shadow: var(--shadow-sm); }}
.ds-color {{ height: 140px; width: 100%; }}
.ds-color-info {{ padding: 20px; background: var(--color-bg-card); display: flex; flex-direction: column; gap: 8px; border-top: 1px solid var(--color-border-default); }}
.ds-color-name {{ font-size: var(--text-14); font-weight: var(--w-bold); color: var(--color-text-primary); text-transform: uppercase; }}
.ds-color-var {{ font-family: monospace; font-size: var(--text-12); color: var(--color-text-muted); background: var(--color-bg-elevated); padding: 6px 10px; border-radius: var(--r-sm); display: inline-block; width: max-content; }}
.ds-card-demo {{ background: var(--color-bg-page); padding: 48px; border-radius: var(--r-xl); border: 1px solid var(--color-border-default); display: flex; flex-direction: column; gap: 32px; align-items: flex-start; }}
.ds-card-dark {{ background: var(--color-bg-section); padding: 48px; border-radius: var(--r-xl); border: 1px solid var(--color-border-default); display: flex; flex-direction: column; gap: 32px; align-items: flex-start; }}
.ds-card-accent {{ background: var(--color-bg-card); border: 1px solid var(--color-border-default); padding: 48px; border-radius: var(--r-xl); width: 100%; }}
.ds-text-showcase {{ display: flex; flex-direction: column; gap: 40px; width: 100%; }}
.ds-code {{ display: block; width: 100%; maxWidth: 100%; background: var(--color-bg-elevated); padding: 24px; border-radius: var(--r-md); font-family: monospace; font-size: var(--text-13); color: var(--color-text-secondary); overflow-x: auto; margin-top: 16px; border: 1px solid var(--color-border-subtle); white-space: pre; line-height: 1.6; }}
.ds-row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; width: 100%; }}
</style>
</head>
<body style="background: var(--color-bg-primary); color: var(--color-text-secondary);">

<div class="ds-container">
  
  <header style="margin-bottom: 120px; text-align: center;">
    <div style="font-size: var(--text-14); letter-spacing: var(--ls-widest); text-transform: uppercase; color: var(--color-accent); font-weight: var(--w-bold); margin-bottom: 24px; display: inline-flex; align-items: center; gap: 8px;">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="8" fill="currentColor"/></svg>
      Documentação Oficial
    </div>
    <h1 style="font-family: var(--font-display); font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: var(--w-black); color: var(--color-text-primary); letter-spacing: var(--ls-tighter); line-height: 1.1;">
      Design System<br>
      <span style="background: var(--gradient-metal-light); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Premium Dark</span>
    </h1>
    <p style="font-size: var(--text-20); color: var(--color-text-muted); margin: 32px auto 0; max-width: 700px; line-height: var(--lh-relaxed);">
      Guia de estilos interativo com todos os tokens, tipografia, botões e componentes estruturais. Copie e cole essas classes em projetos futuros.
    </p>
  </header>

  <section class="ds-section">
    <h2 class="ds-title">1. Tokens Globais (Cores Base)</h2>
    <div class="ds-grid">
      <!-- Surfaces -->
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-bg-page);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Background Page</span>
          <span class="ds-color-var">--color-bg-page</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-bg-primary);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Background Primary</span>
          <span class="ds-color-var">--color-bg-primary</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-bg-section);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Background Section</span>
          <span class="ds-color-var">--color-bg-section</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-bg-card);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Background Card</span>
          <span class="ds-color-var">--color-bg-card</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-bg-elevated);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Background Elevated</span>
          <span class="ds-color-var">--color-bg-elevated</span>
        </div>
      </div>
      
      <!-- Accent -->
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-accent);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Accent Primary</span>
          <span class="ds-color-var">--color-accent</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-gradient-accent);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Gradient Accent</span>
          <span class="ds-color-var">--color-gradient-accent</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-accent-subtle);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Accent Subtle</span>
          <span class="ds-color-var">--color-accent-subtle</span>
        </div>
      </div>
    </div>
  </section>

  <section class="ds-section">
    <h2 class="ds-title">2. Text Cores (Typography Tokens)</h2>
    <div class="ds-grid">
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-text-primary);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Text Primary</span>
          <span class="ds-color-var">--color-text-primary</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-text-secondary);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Text Secondary</span>
          <span class="ds-color-var">--color-text-secondary</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-text-muted);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Text Muted</span>
          <span class="ds-color-var">--color-text-muted</span>
        </div>
      </div>
      <div class="ds-swatch">
        <div class="ds-color" style="background: var(--color-text-disabled);"></div>
        <div class="ds-color-info">
          <span class="ds-color-name">Text Disabled</span>
          <span class="ds-color-var">--color-text-disabled</span>
        </div>
      </div>
    </div>
  </section>

  <section class="ds-section">
    <h2 class="ds-title">3. Tipografia Genérica</h2>
    <div class="ds-card-demo">
      <div class="ds-text-showcase">
        <div>
          <span style="font-size: var(--text-12); color: var(--color-text-muted); font-family: monospace; margin-bottom: 8px; display: block;">Super Headline (var(--text-64))</span>
          <h1 style="font-family: var(--font-display); font-size: var(--text-64); font-weight: var(--w-black); color: var(--color-text-primary); letter-spacing: var(--ls-tighter); line-height: var(--lh-none);">The quick brown fox</h1>
        </div>
        <div>
          <span style="font-size: var(--text-12); color: var(--color-text-muted); font-family: monospace; margin-bottom: 8px; display: block;">Classe .section-h2 normal</span>
          <h2 class="section-h2" style="margin:0; text-align: left;">Estilo de Seção Principal</h2>
        </div>
        <div>
          <span style="font-size: var(--text-12); color: var(--color-text-muted); font-family: monospace; margin-bottom: 8px; display: block;">Classe .section-h2 com &lt;em&gt; ativo</span>
          <h2 class="section-h2" style="margin:0; text-align: left;">Destaque com <em>Cor de Ênfase</em></h2>
        </div>
        <div>
          <span style="font-size: var(--text-12); color: var(--color-text-muted); font-family: monospace; margin-bottom: 8px; display: block;">Classe .section-h2 com ".metal"</span>
          <h2 class="section-h2" style="margin:0; text-align: left;">Destaque <span class="metal">Metálico Prata</span></h2>
        </div>
         <div>
          <span style="font-size: var(--text-12); color: var(--color-text-muted); font-family: monospace; margin-bottom: 8px; display: block;">Classe .section-sub</span>
          <p class="section-sub" style="margin:0; max-width: 800px; text-align: left;">
            Corpo de texto padrão em seções. Usado para descrições, leitura contínua e detalhamento de blocos de conteúdo com line-height relaxado para excelente legibilidade mesmo no tema escuro. O contraste foi perfeitamente balanceado.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="ds-section">
    <h2 class="ds-title">4. Estilos de Botão</h2>
    <div class="ds-card-dark">
      <div class="ds-row">
        <button class="btn btn-primary btn-xl">
          Botão Primary XL
        </button>
        <button class="btn btn-primary btn-lg">
          Primary LG
        </button>
        <button class="btn btn-primary btn-md">
          Primary MD
        </button>
        <button class="btn btn-primary btn-sm">
          SM
        </button>
      </div>
      <div class="ds-row">
        <button class="btn btn-primary btn-md">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 1V11M8 11L5 8M8 11L11 8M2 13H14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Com Ícone SVG Integrado
        </button>
      </div>
      
      <hr style="width: 100%; border: none; border-top: 1px solid var(--color-border-subtle); margin: 16px 0;">
      
      <div class="ds-row">
        <button class="btn btn-outline btn-xl">Botão Outline XL</button>
        <button class="btn btn-outline btn-lg">Outline LG</button>
        <button class="btn btn-outline btn-md">Outline MD</button>
      </div>
      
      <hr style="width: 100%; border: none; border-top: 1px solid var(--color-border-subtle); margin: 16px 0;">

      <div class="ds-row">
        <button class="btn btn-ghost btn-xl">Botão Ghost XL</button>
        <button class="btn btn-ghost btn-lg">Ghost LG</button>
        <button class="btn btn-ghost btn-md">Ghost MD</button>
      </div>

      <hr style="width: 100%; border: none; border-top: 1px solid var(--color-border-subtle); margin: 16px 0;">

      <div class="ds-row">
        <button class="btn btn-text">
          Link de Texto Acionável
          <svg width="16" height="16" viewBox="0 0 20 20" fill="none"><path d="M10 4V16M10 16L6 12M10 16L14 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </div>
<div class="ds-code">
&lt;!-- Códigos HTML Padrão --&gt;
&lt;button class="btn btn-primary btn-md"&gt;Salvar Tudo&lt;/button&gt;
&lt;button class="btn btn-outline btn-md"&gt;Cancelar&lt;/button&gt;
&lt;a href="#" class="btn btn-text"&gt;Ler mais detalhes&lt;/a&gt;
</div>
  </section>

  <section class="ds-section">
    <h2 class="ds-title">5. Badges, Notificações & Detalhes</h2>
    <div class="ds-card-demo">
      <div class="ds-row">
        <div class="hero-tag">
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><circle cx="5" cy="5" r="5" fill="currentColor"/></svg>
          Tag de Destaque Simples
        </div>
      </div>
      <div class="ds-row">
        <div class="section-overline">
          Overline para Cabeçalho de Seção
        </div>
      </div>
      <div class="ds-row">
        <div class="premium-tag">
           <span class="premium-tag-badge">NOVO</span>
           Badge Acoplada a um contexto maior
        </div>
      </div>
      <div class="ds-row">
        <div class="hero-price-block">
           <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 1L8.5 5.5H13L9.5 8L10.5 12.5L7 10L3.5 12.5L4.5 8L1 5.5H5.5L7 1Z" fill="currentColor"/></svg>
           Etiqueta Categórica (Ex: Pricing)
        </div>
      </div>
    </div>
  </section>

  <section class="ds-section">
    <h2 class="ds-title">6. Componentes Reutilizáveis (Cards UI)</h2>
    <div class="ds-card-dark">
      <!-- Módulos Card -->
      <h3 style="color: var(--color-text-primary); font-family: var(--font-display); margin-bottom: 24px;">Card de Módulo/Funcionalidade</h3>
      <article class="modulo-card" style="width: 320px;">
        <div class="modulo-number">Item Num</div>
        <h3 class="modulo-title">Título do Modulo / Card</h3>
        <div class="modulo-topics">
          <div class="modulo-topic"><div class="modulo-topic-dot"></div>Item da lista ponto 1</div>
          <div class="modulo-topic"><div class="modulo-topic-dot"></div>Item da lista ponto 2</div>
          <div class="modulo-topic"><div class="modulo-topic-dot"></div>Item da lista ponto 3</div>
        </div>
      </article>
      
      <div style="height: 24px;"></div>
      
      <!-- Bônus Card -->
      <h3 style="color: var(--color-text-primary); font-family: var(--font-display); margin-bottom: 24px;">Card de Bônus (Destaque Interno)</h3>
      <div class="bonus-card" style="margin-top: 0; max-width: 600px;">
        <div class="bonus-icon">
          <svg width="22" height="22" viewBox="0 0 22 22" fill="none"><path d="M11 2L13.5 8H20L14.5 11.5L16.5 18L11 14.5L5.5 18L7.5 11.5L2 8H8.5L11 2Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
        </div>
        <div>
          <div class="bonus-label">Destaque Label</div>
          <div class="bonus-text">Corpo de texto que explica qual é a oferta ou bônus com destaque visual com background que utiliza um blend de accent.</div>
        </div>
      </div>
      
      <div style="height: 24px;"></div>
      
      <!-- Listas Check -->
      <h3 style="color: var(--color-text-primary); font-family: var(--font-display); margin-bottom: 24px;">Itens de Lista em Grid (Benefícios)</h3>
      <div class="ds-grid" style="grid-template-columns: 1fr 1fr; width: 100%;">
        <div class="para-quem-item" style="margin: 0; align-items: center;">
          <div class="para-quem-check">
            <svg viewBox="0 0 11 9" fill="none"><path d="M1 4.5L4 7.5L10 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div class="para-quem-text">Item padrão de check</div>
        </div>
        <div class="topic-item" style="margin: 0;">
          <div class="topic-number">01</div>
          <div class="topic-text">Número de destaque / etapa</div>
        </div>
      </div>
      
<div class="ds-code">
&lt;!-- HTML do Card do Módulo --&gt;
&lt;article class="modulo-card"&gt;
  &lt;div class="modulo-number"&gt;Subtítulo superior&lt;/div&gt;
  &lt;h3 class="modulo-title"&gt;Título Principal&lt;/h3&gt;
&lt;/article&gt;

&lt;!-- HTML da Lista Check --&gt;
&lt;div class="para-quem-item"&gt;
  &lt;div class="para-quem-check"&gt;&lt;svg viewBox="0 0 11 9" fill="none"&gt;&lt;path d="..." stroke="currentColor" /&gt;&lt;/svg&gt;&lt;/div&gt;
  &lt;div class="para-quem-text"&gt;Texto ao lado do check&lt;/div&gt;
&lt;/div&gt;
</div>

    </div>
  </section>

  <section class="ds-section">
    <h2 class="ds-title">7. Painel de Acordeão (Accordion / FAQ)</h2>
    <div class="ds-card-demo">
      <div class="faq-list" style="width: 100%; max-width: 800px; margin: 0;">
        <div class="faq-item">
          <button class="faq-question">
             Exemplo de acordeão fechado?
            <svg class="faq-arrow" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M5 7.5L10 12.5L15 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
        <div class="faq-item open">
          <button class="faq-question" style="color: var(--color-accent);">
            Como funciona o accordion quando ele está aberto?
            <svg class="faq-arrow" style="transform: rotate(180deg);" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M5 7.5L10 12.5L15 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <div class="faq-answer" style="max-height: 200px;">
            <div class="faq-answer-inner">No Javascript, ao clicar, aplicamos a classe `.open` no elemento pai `.faq-item`. Isso fará com que o texto interno seja exibido e o ícone rotacione perfeitamente com transições CSS suaves.</div>
          </div>
        </div>
      </div>
      
<div class="ds-code">
&lt;!-- HTML do Item Acordeão --&gt;
&lt;div class="faq-item"&gt;
  &lt;button class="faq-question"&gt;
    Pergunta Aqui
    &lt;svg class="faq-arrow" ...&gt;&lt;/svg&gt;
  &lt;/button&gt;
  &lt;div class="faq-answer"&gt;
    &lt;div class="faq-answer-inner"&gt;Resposta detalhada vai aqui.&lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;
</div>
    </div>
  </section>

</div>

</body>
</html>
"""

with open(html_output, "w", encoding="utf-8") as f:
    f.write(html_docs)

print(f"Exportado com sucesso para: {html_output}")
