%%
P: S Q;
Q: %empty | P;
S: "if" E "then" S R | "while" E S | "begin" P "end" | "print" E | E;
R: %empty | "else" S;
E: "id" | "entero" | "id" F | "entero" F;
F: "+" E | "+" E F;
