import { useState, useEffect, useRef, useCallback } from "react";

const SYSTEM_PROMPT = `Sos "Profe Alex", un profesor de inglés británico de élite que trabaja con alumnos latinoamericanos para llevarlos de B1 a B2 (Cambridge First Certificate). Tu personalidad: exigente pero cálido, directo, motivador, enfocado en resultados. Nunca sos complaciente. Siempre corregís errores de forma clara y constructiva.

PERFIL DEL ALUMNO:
- Nivel actual: B1 (intermedio bajo)
- Debilidades: gramática, fluidez, conectar oraciones
- Prioridad: speaking > listening > vocabulario > gramática > writing
- Objetivo: Cambridge First Certificate (B2)
- Inglés: británico
- Contexto profesional: negocios/legal/finanzas

──────────────────────────────────────────
🗣️ FORMATO DE COMUNICACIÓN (MUY IMPORTANTE)
──────────────────────────────────────────
Usás una mezcla natural de español latinoamericano + inglés, así:

• Las INSTRUCCIONES, CONTEXTO y EXPLICACIONES van en español (rioplatense/neutro latino). Usás "vos", "dale", "buenísimo", "che" ocasionalmente.
• El CONTENIDO A PRACTICAR (preguntas, frases, roleplays, vocabulario) va en INGLÉS.
• Las CORRECCIONES siguen este formato bilingüe:
   ❌ Lo que dijo: "I go to the work yesterday"
   ✅ Correcto: "I went to work yesterday"
   💡 "Went" es el pasado irregular de "go". Y "work" sin artículo cuando es lugar rutinario.
   🔁 Ahora repetilo vos: "Yesterday, I went to work and..."

• Cuando hacés preguntas de speaking, las escribís en inglés Y dás una guía en español de qué se espera.
• Las palabras/frases nuevas las presentás así: **"commute"** → el trayecto al trabajo (ej: "My daily commute takes 40 minutes")

──────────────────────────────────────────
REGLAS DE ENSEÑANZA:
──────────────────────────────────────────
1. Empujá siempre al alumno a producir lenguaje — no dejes que pase más de 2 mensajes sin que hable/escriba en inglés.
2. Si el alumno responde en español cuando debería hacerlo en inglés, lo redirigís amablemente: "Dale, eso decilo en inglés — te ayudo si necesitás."
3. Conectá la gramática con lo que el alumno quiso decir, nunca la enseñes en abstracto.
4. Trabajá mucho: linking words (however, although, in addition, as a result), naturalidad, velocidad progresiva.
5. Nunca des clases magistrales largas. Explicaciones de máximo 3 oraciones.
6. Siempre terminá tu turno con una pregunta o tarea que fuerce producción.

──────────────────────────────────────────
ESTRUCTURA DE CADA CLASE:
──────────────────────────────────────────
Fase 1 - WARM-UP: 2-3 preguntas para entrar en calor
Fase 2 - SPEAKING PRINCIPAL: tema guiado o roleplay
Fase 3 - CORRECCIONES CLAVE: errores principales de la clase
Fase 4 - MINI INPUT: punto de gramática/vocabulario si hace falta
Fase 5 - SPEAKING MEJORADO: reintento aplicando correcciones
Fase 6 - CIERRE + FEEDBACK: resumen breve de la sesión
Fase 7 - TAREA: una tarea corta y específica

──────────────────────────────────────────
TEST DE NIVELACIÓN (solo primera sesión):
──────────────────────────────────────────
Cuando sea la primera clase:
1. Hacé 3 preguntas de speaking (trabajo/rutina, motivos para aprender inglés, problema reciente resuelto)
2. Dá 5 oraciones con gap-fill de gramática
3. Pedile que escriba 3-4 oraciones sobre un tema dado
4. Evaluá su rango de vocabulario
Luego entregá evaluación detallada con: nivel estimado, fortalezas, debilidades, top 5 errores recurrentes, plan personalizado hasta B2, tiempo estimado.

──────────────────────────────────────────
AL FINALIZAR CADA CLASE:
──────────────────────────────────────────
Cuando el alumno diga "terminar clase", "end class" o pida feedback, generá el resumen en este JSON exacto dentro de tags <SESSION_DATA>:
<SESSION_DATA>
{
  "phase_completed": "nombre de la fase",
  "errors_found": ["error1", "error2"],
  "vocab_learned": ["palabra - definición en español", "palabra - definición"],
  "level_update": "B1 / B1+ / B1-B2 / B2-",
  "strengths_today": "qué salió bien",
  "focus_next": "qué trabajar en la próxima clase",
  "homework": "tarea específica y concreta"
}
</SESSION_DATA>

──────────────────────────────────────────
EJEMPLOS DE TONO:
──────────────────────────────────────────
- "Buen intento — pero vamos a afilarlo un poco. Fijate en esto:"
- "Casi perfecto, solo una cosa: [corrección]"
- "Dale, podés hacerlo mejor. Intentalo de nuevo."
- "¡Excelente! Eso sonó muy natural."
- "Bueno, te voy a exigir un poco más ahora."
- "Perfecto. Ahora usá eso en una oración completa."

Recordá: tu objetivo no es solo enseñar inglés. Es que este alumno hable cada vez más rápido, mejor y con más confianza en cada sesión.`;

const COLORS = {
  bg: "#0d0f14",
  surface: "#13151c",
  card: "#1a1d26",
  border: "#252836",
  gold: "#d4a853",
  goldLight: "#e8c57a",
  cream: "#f0e8d5",
  muted: "#7a7f95",
  accent: "#4a9eff",
  success: "#4ecdc4",
  error: "#ff6b6b",
};

const FONT_LINK = `@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');`;

const globalStyles = `
  ${FONT_LINK}
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html, body, #root { height: 100%; width: 100%; overflow: hidden; }
  body {
    background: ${COLORS.bg};
    color: ${COLORS.cream};
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.6;
  }
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: ${COLORS.border}; border-radius: 2px; }
  textarea, input { font-family: 'DM Sans', sans-serif; }
  button { cursor: pointer; font-family: 'DM Sans', sans-serif; }

  @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
  
  .msg-enter { animation: fadeIn 0.3s ease forwards; }
  .typing-dot { animation: pulse 1.2s ease infinite; }
  .typing-dot:nth-child(2) { animation-delay: 0.2s; }
  .typing-dot:nth-child(3) { animation-delay: 0.4s; }
`;

// ─── Storage helpers ──────────────────────────────────────────────────────────
async function storageGet(key) {
  try { const r = await window.storage.get(key); return r ? JSON.parse(r.value) : null; }
  catch { return null; }
}
async function storageSet(key, value) {
  try { await window.storage.set(key, JSON.stringify(value)); } catch {}
}

// ─── Anthropic API ────────────────────────────────────────────────────────────
async function callClaude(messages) {
  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 1000,
      system: SYSTEM_PROMPT,
      messages,
    }),
  });
  const data = await res.json();
  return data.content?.[0]?.text || "Sorry, I couldn't respond. Please try again.";
}

// ─── Icons ────────────────────────────────────────────────────────────────────
const Icon = ({ name, size = 18, color = "currentColor" }) => {
  const icons = {
    home: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>,
    chat: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>,
    chart: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/></svg>,
    book: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg>,
    send: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22,2 15,22 11,13 2,9"/></svg>,
    star: <svg width={size} height={size} viewBox="0 0 24 24" fill={color} stroke="none"><polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"/></svg>,
    check: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><polyline points="20,6 9,17 4,12"/></svg>,
    clock: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>,
    trophy: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><polyline points="8,21 12,21 16,21"/><line x1="12" y1="17" x2="12" y2="21"/><path d="M7 4H17L16 10C16 12.21 14.21 14 12 14C9.79 14 8 12.21 8 10L7 4Z"/><path d="M7 4C7 4 5 4 4 6C3 8 4 10 7 10"/><path d="M17 4C17 4 19 4 20 6C21 8 20 10 17 10"/></svg>,
    lightning: <svg width={size} height={size} viewBox="0 0 24 24" fill={color} stroke="none"><polygon points="13,2 3,14 12,14 11,22 21,10 12,10"/></svg>,
    pencil: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>,
  };
  return icons[name] || null;
};

// ─── Level Badge ──────────────────────────────────────────────────────────────
const LevelBadge = ({ level }) => {
  const color = level?.includes("B2") ? COLORS.success : level?.includes("B1+") ? COLORS.gold : COLORS.accent;
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", gap: 4,
      padding: "2px 10px", borderRadius: 20,
      background: color + "22", border: `1px solid ${color}44`,
      color, fontSize: 12, fontWeight: 600, letterSpacing: 1,
    }}>{level || "B1"}</span>
  );
};

// ─── Stat Card ─────────────────────────────────────────────────────────────────
const StatCard = ({ icon, label, value, accent }) => (
  <div style={{
    background: COLORS.card, border: `1px solid ${COLORS.border}`,
    borderRadius: 12, padding: "16px 20px",
    display: "flex", alignItems: "center", gap: 14,
    transition: "border-color 0.2s",
  }}>
    <div style={{
      width: 40, height: 40, borderRadius: 10,
      background: (accent || COLORS.gold) + "18",
      display: "flex", alignItems: "center", justifyContent: "center",
      flexShrink: 0,
    }}>
      <Icon name={icon} size={18} color={accent || COLORS.gold} />
    </div>
    <div>
      <div style={{ fontSize: 22, fontWeight: 700, color: COLORS.cream, fontFamily: "'Playfair Display', serif" }}>{value}</div>
      <div style={{ fontSize: 12, color: COLORS.muted, marginTop: 1 }}>{label}</div>
    </div>
  </div>
);

// ─── Message Bubble ────────────────────────────────────────────────────────────
const MessageBubble = ({ msg }) => {
  const isUser = msg.role === "user";

  const formatText = (text) => {
    return text.split("\n").map((line, i) => {
      const styled = line
        .replace(/❌\s*(.*)/g, `<span style="color:${COLORS.error};font-weight:500">❌ $1</span>`)
        .replace(/✅\s*(.*)/g, `<span style="color:${COLORS.success};font-weight:500">✅ $1</span>`)
        .replace(/💡\s*(.*)/g, `<span style="color:${COLORS.gold};font-style:italic">💡 $1</span>`)
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/\*(.*?)\*/g, "<em>$1</em>");
      return <p key={i} dangerouslySetInnerHTML={{ __html: styled }} style={{ marginBottom: i < text.split("\n").length - 1 ? 6 : 0 }} />;
    });
  };

  return (
    <div className="msg-enter" style={{
      display: "flex", justifyContent: isUser ? "flex-end" : "flex-start",
      marginBottom: 16, alignItems: "flex-end", gap: 8,
    }}>
      {!isUser && (
        <div style={{
          width: 32, height: 32, borderRadius: "50%",
          background: `linear-gradient(135deg, ${COLORS.gold} 0%, #b8892a 100%)`,
          display: "flex", alignItems: "center", justifyContent: "center",
          flexShrink: 0, fontSize: 13, fontWeight: 700, color: "#1a0f00",
          fontFamily: "'Playfair Display', serif",
        }}>A</div>
      )}
      <div style={{
        maxWidth: "75%",
        background: isUser
          ? `linear-gradient(135deg, ${COLORS.gold}dd 0%, #b8892a 100%)`
          : COLORS.card,
        color: isUser ? "#1a0f00" : COLORS.cream,
        padding: "12px 16px", borderRadius: isUser ? "18px 18px 4px 18px" : "18px 18px 18px 4px",
        border: isUser ? "none" : `1px solid ${COLORS.border}`,
        fontSize: 14, lineHeight: 1.65,
        boxShadow: "0 2px 12px rgba(0,0,0,0.3)",
      }}>
        {formatText(msg.content.replace(/<SESSION_DATA>[\s\S]*?<\/SESSION_DATA>/g, "").trim())}
        <div style={{ fontSize: 11, opacity: 0.5, marginTop: 4, textAlign: "right" }}>
          {msg.time}
        </div>
      </div>
      {isUser && (
        <div style={{
          width: 32, height: 32, borderRadius: "50%",
          background: COLORS.border,
          display: "flex", alignItems: "center", justifyContent: "center",
          flexShrink: 0, fontSize: 13, fontWeight: 700, color: COLORS.muted,
        }}>Y</div>
      )}
    </div>
  );
};

// ─── Typing Indicator ─────────────────────────────────────────────────────────
const TypingIndicator = () => (
  <div style={{ display: "flex", alignItems: "flex-end", gap: 8, marginBottom: 16 }}>
    <div style={{
      width: 32, height: 32, borderRadius: "50%",
      background: `linear-gradient(135deg, ${COLORS.gold} 0%, #b8892a 100%)`,
      display: "flex", alignItems: "center", justifyContent: "center",
      flexShrink: 0, fontSize: 13, fontWeight: 700, color: "#1a0f00",
      fontFamily: "'Playfair Display', serif",
    }}>A</div>
    <div style={{
      background: COLORS.card, border: `1px solid ${COLORS.border}`,
      padding: "14px 18px", borderRadius: "18px 18px 18px 4px",
      display: "flex", gap: 5, alignItems: "center",
    }}>
      {[0, 1, 2].map((i) => (
        <div key={i} className="typing-dot" style={{
          width: 7, height: 7, borderRadius: "50%",
          background: COLORS.gold, animationDelay: `${i * 0.2}s`,
        }} />
      ))}
    </div>
  </div>
);

// ─── Progress View ────────────────────────────────────────────────────────────
const ProgressView = ({ sessions, profile }) => {
  const allErrors = sessions.flatMap((s) => s.errors_found || []);
  const errorCount = {};
  allErrors.forEach((e) => { errorCount[e] = (errorCount[e] || 0) + 1; });
  const topErrors = Object.entries(errorCount).sort((a, b) => b[1] - a[1]).slice(0, 5);

  const allVocab = sessions.flatMap((s) => s.vocab_learned || []);
  const uniqueVocab = [...new Set(allVocab)];

  return (
    <div style={{ padding: "24px 28px", overflowY: "auto", height: "100%" }}>
      <h2 style={{ fontFamily: "'Playfair Display', serif", fontSize: 24, color: COLORS.cream, marginBottom: 6 }}>Your Progress</h2>
      <p style={{ color: COLORS.muted, marginBottom: 24 }}>Track your journey to B2</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 12, marginBottom: 24 }}>
        <StatCard icon="book" label="Classes completed" value={sessions.length} />
        <StatCard icon="lightning" label="Words learned" value={uniqueVocab.length} accent={COLORS.accent} />
        <StatCard icon="trophy" label="Current level" value={profile?.current_level || "B1"} accent={COLORS.success} />
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        <div style={{ background: COLORS.card, border: `1px solid ${COLORS.border}`, borderRadius: 12, padding: 20 }}>
          <h3 style={{ fontFamily: "'Playfair Display', serif", fontSize: 16, marginBottom: 14, color: COLORS.gold }}>🔴 Common Errors</h3>
          {topErrors.length === 0 ? (
            <p style={{ color: COLORS.muted, fontSize: 13 }}>No errors recorded yet.</p>
          ) : topErrors.map(([err, count], i) => (
            <div key={i} style={{
              display: "flex", justifyContent: "space-between", alignItems: "center",
              padding: "8px 0", borderBottom: i < topErrors.length - 1 ? `1px solid ${COLORS.border}` : "none",
            }}>
              <span style={{ fontSize: 13, color: COLORS.cream }}>{err}</span>
              <span style={{
                fontSize: 11, padding: "2px 8px", borderRadius: 10,
                background: COLORS.error + "22", color: COLORS.error, fontWeight: 600,
              }}>×{count}</span>
            </div>
          ))}
        </div>

        <div style={{ background: COLORS.card, border: `1px solid ${COLORS.border}`, borderRadius: 12, padding: 20 }}>
          <h3 style={{ fontFamily: "'Playfair Display', serif", fontSize: 16, marginBottom: 14, color: COLORS.gold }}>📚 Vocabulary Bank</h3>
          {uniqueVocab.length === 0 ? (
            <p style={{ color: COLORS.muted, fontSize: 13 }}>No vocabulary recorded yet.</p>
          ) : (
            <div style={{ maxHeight: 200, overflowY: "auto" }}>
              {uniqueVocab.slice(-15).reverse().map((v, i) => (
                <div key={i} style={{
                  fontSize: 13, padding: "5px 0",
                  borderBottom: i < Math.min(uniqueVocab.length - 1, 14) ? `1px solid ${COLORS.border}` : "none",
                  color: COLORS.cream,
                }}>
                  <span style={{ color: COLORS.gold }}>•</span> {v}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {sessions.length > 0 && (
        <div style={{ background: COLORS.card, border: `1px solid ${COLORS.border}`, borderRadius: 12, padding: 20, marginTop: 16 }}>
          <h3 style={{ fontFamily: "'Playfair Display', serif", fontSize: 16, marginBottom: 14, color: COLORS.gold }}>📋 Session History</h3>
          {sessions.slice(-8).reverse().map((s, i) => (
            <div key={i} style={{
              padding: "10px 0",
              borderBottom: i < Math.min(sessions.length - 1, 7) ? `1px solid ${COLORS.border}` : "none",
            }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 4 }}>
                <span style={{ fontSize: 13, fontWeight: 500, color: COLORS.cream }}>{s.date}</span>
                <LevelBadge level={s.level_update} />
              </div>
              {s.focus_next && <p style={{ fontSize: 12, color: COLORS.muted }}>Focus next: {s.focus_next}</p>}
              {s.homework && <p style={{ fontSize: 12, color: COLORS.accent }}>HW: {s.homework}</p>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// ─── Dashboard View ───────────────────────────────────────────────────────────
const DashboardView = ({ profile, sessions, onStartLesson }) => {
  const lastSession = sessions[sessions.length - 1];
  const streakDays = sessions.length;

  return (
    <div style={{ padding: "24px 28px", overflowY: "auto", height: "100%" }}>
      <div style={{ marginBottom: 28 }}>
        <h1 style={{
          fontFamily: "'Playfair Display', serif",
          fontSize: 28, fontWeight: 700, color: COLORS.cream,
          marginBottom: 6,
        }}>
          Bienvenido de vuelta. <span style={{ color: COLORS.gold }}>A trabajar.</span>
        </h1>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <LevelBadge level={profile?.current_level || "B1"} />
          <span style={{ color: COLORS.muted, fontSize: 13 }}>→ Target: B2 First Certificate</span>
        </div>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 12, marginBottom: 24 }}>
        <StatCard icon="book" label="Clases completadas" value={sessions.length} />
        <StatCard icon="clock" label="Racha de días" value={`${streakDays}d`} accent={COLORS.accent} />
        <StatCard icon="trophy" label="Nivel" value={profile?.current_level || "B1"} accent={COLORS.success} />
      </div>

      <button onClick={onStartLesson} style={{
        width: "100%", padding: "18px 24px",
        background: `linear-gradient(135deg, ${COLORS.gold} 0%, #b8892a 100%)`,
        border: "none", borderRadius: 14, color: "#1a0f00",
        fontSize: 16, fontWeight: 700, cursor: "pointer",
        display: "flex", alignItems: "center", justifyContent: "center", gap: 10,
        marginBottom: 24, boxShadow: `0 4px 24px ${COLORS.gold}44`,
        transition: "transform 0.15s, box-shadow 0.15s",
        fontFamily: "'DM Sans', sans-serif",
      }}
        onMouseEnter={(e) => { e.target.style.transform = "translateY(-1px)"; e.target.style.boxShadow = `0 6px 28px ${COLORS.gold}66`; }}
        onMouseLeave={(e) => { e.target.style.transform = "translateY(0)"; e.target.style.boxShadow = `0 4px 24px ${COLORS.gold}44`; }}
      >
        <Icon name="chat" size={20} color="#1a0f00" />
        {sessions.length === 0 ? "Empezar Test de Nivelación" : "Empezar la Clase de Hoy"}
      </button>

      {lastSession && (
        <div style={{ background: COLORS.card, border: `1px solid ${COLORS.border}`, borderRadius: 12, padding: 20, marginBottom: 16 }}>
          <h3 style={{ fontFamily: "'Playfair Display', serif", fontSize: 15, color: COLORS.gold, marginBottom: 12 }}>📌 De la última clase</h3>
          {lastSession.homework && (
            <div style={{ marginBottom: 10 }}>
              <span style={{ fontSize: 11, color: COLORS.muted, textTransform: "uppercase", letterSpacing: 1 }}>Tarea pendiente</span>
              <p style={{ fontSize: 13, color: COLORS.cream, marginTop: 4 }}>{lastSession.homework}</p>
            </div>
          )}
          {lastSession.focus_next && (
            <div>
              <span style={{ fontSize: 11, color: COLORS.muted, textTransform: "uppercase", letterSpacing: 1 }}>Foco de hoy</span>
              <p style={{ fontSize: 13, color: COLORS.accent, marginTop: 4 }}>{lastSession.focus_next}</p>
            </div>
          )}
        </div>
      )}

      {profile?.weaknesses && (
        <div style={{ background: COLORS.card, border: `1px solid ${COLORS.border}`, borderRadius: 12, padding: 20 }}>
          <h3 style={{ fontFamily: "'Playfair Display', serif", fontSize: 15, color: COLORS.gold, marginBottom: 12 }}>⚡ Tu perfil</h3>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
            <div>
              <span style={{ fontSize: 11, color: COLORS.muted, textTransform: "uppercase", letterSpacing: 1 }}>Fortalezas</span>
              <p style={{ fontSize: 13, color: COLORS.success, marginTop: 4 }}>{profile.strengths || "—"}</p>
            </div>
            <div>
              <span style={{ fontSize: 11, color: COLORS.muted, textTransform: "uppercase", letterSpacing: 1 }}>Trabajando en</span>
              <p style={{ fontSize: 13, color: COLORS.error, marginTop: 4 }}>{profile.weaknesses || "—"}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

// ─── Lesson (Chat) View ───────────────────────────────────────────────────────
const LessonView = ({ initialMessages, onSessionEnd, sessionCount }) => {
  const [messages, setMessages] = useState(initialMessages || []);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);
  const textareaRef = useRef(null);

  const now = () => new Date().toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" });

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  useEffect(() => {
    if (messages.length === 0) {
      const greeting = sessionCount === 0
        ? `¡Bienvenido! Soy el Profe Alex. 🎯

Antes de arrancar con las clases, necesito ver tu inglés real. Vamos a hacer un **test de nivelación** rápido — sin traductor, sin correcciones previas, sin preparación. Quiero ver cómo hablás naturalmente.

Empecemos. Respondé esto en inglés, como puedas:

**"Tell me about yourself — who are you, what do you do, and what does a typical day look like for you?"**

_No lo pienses demasiado. Con errores y todo está bien — eso es exactamente lo que necesito ver. ¡Dale!_ 💪`
        : `¡Buenas! Profe Alex acá. 🎯

Antes de arrancar — ¿hiciste la tarea de la clase pasada? Contame qué hiciste, **en inglés**.

Y después calentamos motores: **"What have you been up to this week? Tell me something interesting that happened."**

_Acordate de conectar tus ideas — first, then, however, as a result... ¡Dale!_`;

      const firstMsg = {
        role: "assistant",
        content: greeting,
        time: now(),
      };
      setMessages([firstMsg]);
    }
  }, []);

  const sendMessage = useCallback(async () => {
    if (!input.trim() || loading) return;
    const userMsg = { role: "user", content: input.trim(), time: now() };
    const newMessages = [...messages, userMsg];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    try {
      const apiMessages = newMessages.map((m) => ({ role: m.role, content: m.content }));
      const reply = await callClaude(apiMessages);

      const assistantMsg = { role: "assistant", content: reply, time: now() };
      setMessages((prev) => [...prev, assistantMsg]);

      // Check for session data
      const match = reply.match(/<SESSION_DATA>([\s\S]*?)<\/SESSION_DATA>/);
      if (match) {
        try {
          const sessionData = JSON.parse(match[1].trim());
          onSessionEnd([...newMessages, assistantMsg], sessionData);
        } catch {}
      }
    } catch {
      setMessages((prev) => [...prev, {
        role: "assistant",
        content: "I had a connection issue. Please try sending that again.",
        time: now(),
      }]);
    }
    setLoading(false);
  }, [input, messages, loading, onSessionEnd]);

  const handleKey = (e) => {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  };

  const quickActions = [
    { label: "Terminar clase 📋", msg: "terminar clase" },
    { label: "Ayudame a decirlo mejor", msg: "Can you help me say that better? Give me a more natural way." },
    { label: "Más difícil por favor", msg: "Make it more challenging, push me harder." },
    { label: "Explicame en español", msg: "Explicame eso en español, no entendí bien." },
  ];

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100%", padding: "0 0 0 0" }}>
      {/* Header */}
      <div style={{
        padding: "14px 24px", borderBottom: `1px solid ${COLORS.border}`,
        display: "flex", alignItems: "center", justifyContent: "space-between",
        background: COLORS.surface, flexShrink: 0,
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <div style={{
            width: 36, height: 36, borderRadius: "50%",
            background: `linear-gradient(135deg, ${COLORS.gold} 0%, #b8892a 100%)`,
            display: "flex", alignItems: "center", justifyContent: "center",
            fontSize: 14, fontWeight: 700, color: "#1a0f00",
            fontFamily: "'Playfair Display', serif",
          }}>A</div>
          <div>
            <div style={{ fontSize: 14, fontWeight: 600, color: COLORS.cream }}>Profe Alex</div>
            <div style={{ fontSize: 11, color: COLORS.success, display: "flex", alignItems: "center", gap: 4 }}>
              <div style={{ width: 6, height: 6, borderRadius: "50%", background: COLORS.success }} />
              En línea · Inglés Británico
            </div>
          </div>
        </div>
        <div style={{ fontSize: 11, color: COLORS.muted, background: COLORS.card, padding: "4px 10px", borderRadius: 8, border: `1px solid ${COLORS.border}` }}>
          Class #{sessionCount + 1}
        </div>
      </div>

      {/* Messages */}
      <div style={{ flex: 1, overflowY: "auto", padding: "20px 20px 0 20px" }}>
        {messages.map((msg, i) => <MessageBubble key={i} msg={msg} />)}
        {loading && <TypingIndicator />}
        <div ref={bottomRef} style={{ height: 8 }} />
      </div>

      {/* Quick actions */}
      <div style={{ padding: "8px 20px 0", display: "flex", gap: 6, flexWrap: "wrap", flexShrink: 0 }}>
        {quickActions.map((a, i) => (
          <button key={i} onClick={() => { setInput(a.msg); textareaRef.current?.focus(); }} style={{
            fontSize: 11, padding: "5px 10px", borderRadius: 8,
            background: "transparent", border: `1px solid ${COLORS.border}`,
            color: COLORS.muted, cursor: "pointer",
            transition: "border-color 0.15s, color 0.15s",
          }}
            onMouseEnter={(e) => { e.target.style.borderColor = COLORS.gold; e.target.style.color = COLORS.gold; }}
            onMouseLeave={(e) => { e.target.style.borderColor = COLORS.border; e.target.style.color = COLORS.muted; }}
          >{a.label}</button>
        ))}
      </div>

      {/* Input */}
      <div style={{ padding: "12px 20px 16px", flexShrink: 0 }}>
        <div style={{
          display: "flex", gap: 10, alignItems: "flex-end",
          background: COLORS.card, border: `1px solid ${COLORS.border}`,
          borderRadius: 14, padding: "8px 8px 8px 16px",
          transition: "border-color 0.2s",
        }}>
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKey}
            placeholder="Escribí en inglés… (Enter para enviar, Shift+Enter para nueva línea)"
            style={{
              flex: 1, background: "transparent", border: "none", outline: "none",
              color: COLORS.cream, fontSize: 14, resize: "none",
              minHeight: 40, maxHeight: 120, lineHeight: 1.5,
              "::placeholder": { color: COLORS.muted },
            }}
            rows={1}
          />
          <button onClick={sendMessage} disabled={!input.trim() || loading} style={{
            width: 40, height: 40, borderRadius: 10, border: "none", flexShrink: 0,
            background: input.trim() && !loading
              ? `linear-gradient(135deg, ${COLORS.gold} 0%, #b8892a 100%)`
              : COLORS.border,
            display: "flex", alignItems: "center", justifyContent: "center",
            transition: "background 0.2s, transform 0.15s",
            cursor: input.trim() && !loading ? "pointer" : "default",
          }}>
            <Icon name="send" size={16} color={input.trim() && !loading ? "#1a0f00" : COLORS.muted} />
          </button>
        </div>
        <p style={{ fontSize: 11, color: COLORS.muted, marginTop: 6, textAlign: "center" }}>
          Type <strong style={{ color: COLORS.gold }}>&quot;terminar clase&quot;</strong> cuando quieras el feedback y cerrar la sesión
        </p>
      </div>
    </div>
  );
};

// ─── Main App ─────────────────────────────────────────────────────────────────
export default function App() {
  const [view, setView] = useState("dashboard");
  const [profile, setProfile] = useState(null);
  const [sessions, setSessions] = useState([]);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
      const p = await storageGet("student-profile");
      const s = await storageGet("sessions") || [];
      setProfile(p);
      setSessions(s);
      setLoaded(true);
    })();
  }, []);

  const handleSessionEnd = useCallback(async (messages, sessionData) => {
    const newSession = {
      ...sessionData,
      date: new Date().toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" }),
      message_count: messages.length,
    };
    const updatedSessions = [...sessions, newSession];
    setSessions(updatedSessions);
    await storageSet("sessions", updatedSessions);

    // Update profile
    const updatedProfile = {
      ...(profile || {}),
      current_level: sessionData.level_update || profile?.current_level || "B1",
      last_session: newSession.date,
      weaknesses: sessionData.focus_next || profile?.weaknesses,
      strengths: sessionData.strengths_today || profile?.strengths,
    };
    setProfile(updatedProfile);
    await storageSet("student-profile", updatedProfile);
  }, [sessions, profile]);

  if (!loaded) {
    return (
      <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: COLORS.bg }}>
        <div style={{ textAlign: "center" }}>
          <div style={{ fontFamily: "'Playfair Display', serif", fontSize: 24, color: COLORS.gold, marginBottom: 8 }}>Profe Alex</div>
          <div style={{ color: COLORS.muted, fontSize: 13 }}>Cargando tu perfil…</div>
        </div>
      </div>
    );
  }

  const navItems = [
    { id: "dashboard", icon: "home", label: "Home" },
    { id: "lesson", icon: "chat", label: "Class" },
    { id: "progress", icon: "chart", label: "Progress" },
  ];

  return (
    <>
      <style>{globalStyles}</style>
      <div style={{ display: "flex", height: "100%", background: COLORS.bg }}>
        {/* Sidebar */}
        <div style={{
          width: 200, background: COLORS.surface,
          borderRight: `1px solid ${COLORS.border}`,
          display: "flex", flexDirection: "column",
          padding: "20px 0", flexShrink: 0,
        }}>
          {/* Logo */}
          <div style={{ padding: "0 20px 24px", borderBottom: `1px solid ${COLORS.border}` }}>
            <div style={{ fontFamily: "'Playfair Display', serif", fontSize: 17, fontWeight: 700, color: COLORS.gold }}>
              Prof. Alex
            </div>
            <div style={{ fontSize: 11, color: COLORS.muted, marginTop: 2 }}>B1 → B2 · First Certificate</div>
          </div>

          {/* Nav */}
          <nav style={{ padding: "16px 10px", flex: 1 }}>
            {navItems.map((item) => {
              const active = view === item.id;
              return (
                <button key={item.id} onClick={() => setView(item.id)} style={{
                  width: "100%", display: "flex", alignItems: "center", gap: 10,
                  padding: "10px 12px", borderRadius: 10, border: "none", cursor: "pointer",
                  background: active ? COLORS.gold + "18" : "transparent",
                  color: active ? COLORS.gold : COLORS.muted,
                  fontSize: 14, fontWeight: active ? 600 : 400,
                  marginBottom: 4, transition: "background 0.15s, color 0.15s",
                  textAlign: "left",
                }}>
                  <Icon name={item.icon} size={17} color={active ? COLORS.gold : COLORS.muted} />
                  {item.label}
                </button>
              );
            })}
          </nav>

          {/* Level indicator */}
          <div style={{ padding: "16px 20px", borderTop: `1px solid ${COLORS.border}` }}>
            <div style={{ fontSize: 11, color: COLORS.muted, marginBottom: 6 }}>Current level</div>
            <LevelBadge level={profile?.current_level || "B1"} />
            <div style={{ marginTop: 10 }}>
              <div style={{ display: "flex", justifyContent: "space-between", fontSize: 10, color: COLORS.muted, marginBottom: 4 }}>
                <span>B1</span><span>B2</span>
              </div>
              <div style={{ height: 4, background: COLORS.border, borderRadius: 2 }}>
                <div style={{
                  height: "100%", borderRadius: 2,
                  background: `linear-gradient(90deg, ${COLORS.gold}, ${COLORS.success})`,
                  width: `${Math.min(100, (sessions.length / 40) * 100)}%`,
                  transition: "width 0.5s ease",
                }} />
              </div>
              <div style={{ fontSize: 10, color: COLORS.muted, marginTop: 4, textAlign: "right" }}>
                {sessions.length}/40 classes
              </div>
            </div>
          </div>
        </div>

        {/* Main content */}
        <div style={{ flex: 1, overflow: "hidden", display: "flex", flexDirection: "column" }}>
          {view === "dashboard" && (
            <DashboardView
              profile={profile}
              sessions={sessions}
              onStartLesson={() => setView("lesson")}
            />
          )}
          {view === "lesson" && (
            <LessonView
              key={`lesson-${sessions.length}`}
              sessionCount={sessions.length}
              onSessionEnd={(msgs, data) => { handleSessionEnd(msgs, data); }}
            />
          )}
          {view === "progress" && (
            <ProgressView profile={profile} sessions={sessions} />
          )}
        </div>
      </div>
    </>
  );
}
