
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementleftORleftANDleftEQNEleftGTLTGELEleftPLUSMINUSMODleftTIMESDIVIDEPOWleftASIGNASIGN2AND ARROW ASIGN ASIGN2 COMA CONCAT COS DIVIDE E ELIF ELSE EQ EXP FALSE FOR FUNCTION GE GT ID IF IN LBRACE LE LET LOG LPAREN LT MINUS MOD NE NOT NUMBER OR PI PLUS POW PRINT RAND RANGE RBRACE RPAREN SEMICOLON SIN SQRT STRING TIMES TRUE WHILEstatement : FOR LPAREN ID IN iterable RPAREN statementiterable : RANGE LPAREN NUMBER COMA NUMBER RPARENstatement : WHILE LPAREN expression RPAREN statementexpression : IF LPAREN expression RPAREN expression elifsExp ELSE expressionstatement : IF LPAREN expression RPAREN statement elifs ELSE statementelifs : empty\n            | ELIF LPAREN expression RPAREN statement\n            | elifs ELIF LPAREN expression RPAREN statementelifsExp : empty\n            | ELIF LPAREN expression RPAREN expression\n            | elifsExp ELIF LPAREN expression RPAREN expressionasig : ID ASIGN expressionasig2 : ID ASIGN2 expressionstatement : asig2 SEMICOLONexpression : asig2asigs : asigs COMA asig\n            | asigstatement : LET asigs IN statementexpression : LET asigs IN expressionstatement : LBRACE statements RBRACE\n                | LBRACE statements RBRACE SEMICOLONfunction : ID LPAREN parameters RPARENfunctionDef : FUNCTION ID LPAREN parameters RPAREN ARROW expression SEMICOLON\n                | FUNCTION ID LPAREN RPAREN ARROW expression SEMICOLONfunctionDef : FUNCTION ID LPAREN parameters RPAREN LBRACE statements RBRACE\n                | FUNCTION ID LPAREN RPAREN LBRACE statements RBRACEparameters : parameters COMA expression\n                  | emptyparameters : expressionempty :statements : statements statement\n                  | statementexpression : functionstatement : expression SEMICOLON\n                    | functionDefexpression : factorexpression : expression PLUS expression\n                  | expression MINUS expressionexpression : expression TIMES expression\n            | expression DIVIDE expression\n            | expression POW expression\n            | expression MOD expressionexpression : LPAREN expression RPARENfactor : NUMBER\n              | PI\n              | E\n              | TRUE\n              | FALSE\n              | STRING\n              | IDexpression : SIN LPAREN expression RPAREN\n              | COS LPAREN expression RPAREN\n              | SQRT LPAREN expression RPAREN\n              | EXP LPAREN expression RPAREN\n              | LOG LPAREN expression COMA expression RPAREN\n              | RAND LPAREN RPAREN\n              | PRINT LPAREN expression RPARENexpression : expression EQ expression\n              | expression GT expression\n              | expression LT expression\n              | expression GE expression\n              | expression LE expression\n              | expression NE expressionexpression : expression AND expression\n              | expression OR expressionexpression : NOT expressionexpression : expression CONCAT expression'
    
_lr_action_items = {'FOR':([0,10,11,37,54,58,59,94,97,98,112,113,114,118,132,138,139,150,152,153,158,162,163,164,169,172,173,178,182,],[2,2,-35,-34,-14,2,-32,2,-20,-31,2,2,-18,-21,-3,2,2,2,2,-1,2,2,-24,-26,-5,-23,-25,2,2,]),'WHILE':([0,10,11,37,54,58,59,94,97,98,112,113,114,118,132,138,139,150,152,153,158,162,163,164,169,172,173,178,182,],[5,5,-35,-34,-14,5,-32,5,-20,-31,5,5,-18,-21,-3,5,5,5,5,-1,5,5,-24,-26,-5,-23,-25,5,5,]),'IF':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[7,31,7,-35,31,31,31,31,-34,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-14,7,-32,31,31,31,31,31,31,31,7,31,-20,-31,31,31,31,7,7,-18,-21,31,31,-3,31,7,7,31,7,7,-1,31,31,7,31,7,-24,-26,31,-5,31,-23,-25,31,7,31,7,]),'LET':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[9,33,9,-35,33,33,33,33,-34,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-14,9,-32,33,33,33,33,33,33,33,9,33,-20,-31,33,33,33,9,9,-18,-21,33,33,-3,33,9,9,33,9,9,-1,33,33,9,33,9,-24,-26,33,-5,33,-23,-25,33,9,33,9,]),'LBRACE':([0,10,11,37,54,58,59,94,97,98,112,113,114,118,126,132,136,138,139,150,152,153,158,162,163,164,169,172,173,178,182,],[10,10,-35,-34,-14,10,-32,10,-20,-31,10,10,-18,-21,138,-3,150,10,10,10,10,-1,10,10,-24,-26,-5,-23,-25,10,10,]),'ID':([0,3,9,10,11,21,22,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,95,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[4,4,57,4,-35,4,68,69,57,4,4,4,-34,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-14,4,-32,4,4,4,4,4,4,4,4,57,4,-20,-31,4,4,4,4,4,-18,-21,4,4,-3,4,4,4,4,4,4,-1,4,4,4,4,4,-24,-26,4,-5,4,-23,-25,4,4,4,4,]),'LPAREN':([0,2,3,4,5,7,10,11,14,15,16,17,18,19,20,21,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,68,71,94,96,97,98,106,109,111,112,113,114,118,123,128,129,132,137,138,139,144,147,149,150,152,153,155,156,157,158,159,160,162,163,164,167,169,170,172,173,176,178,180,182,],[3,29,3,35,36,53,3,-35,60,61,62,63,64,65,66,3,71,3,3,3,-34,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-14,3,-32,3,3,3,3,3,3,106,3,3,3,-20,-31,3,3,3,3,3,-18,-21,3,140,3,-3,3,3,3,157,160,3,3,3,-1,3,167,3,3,170,3,3,-24,-26,3,-5,3,-23,-25,3,3,3,3,]),'SIN':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[14,14,14,-35,14,14,14,14,-34,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-14,14,-32,14,14,14,14,14,14,14,14,14,-20,-31,14,14,14,14,14,-18,-21,14,14,-3,14,14,14,14,14,14,-1,14,14,14,14,14,-24,-26,14,-5,14,-23,-25,14,14,14,14,]),'COS':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[15,15,15,-35,15,15,15,15,-34,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-14,15,-32,15,15,15,15,15,15,15,15,15,-20,-31,15,15,15,15,15,-18,-21,15,15,-3,15,15,15,15,15,15,-1,15,15,15,15,15,-24,-26,15,-5,15,-23,-25,15,15,15,15,]),'SQRT':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[16,16,16,-35,16,16,16,16,-34,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-14,16,-32,16,16,16,16,16,16,16,16,16,-20,-31,16,16,16,16,16,-18,-21,16,16,-3,16,16,16,16,16,16,-1,16,16,16,16,16,-24,-26,16,-5,16,-23,-25,16,16,16,16,]),'EXP':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[17,17,17,-35,17,17,17,17,-34,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-14,17,-32,17,17,17,17,17,17,17,17,17,-20,-31,17,17,17,17,17,-18,-21,17,17,-3,17,17,17,17,17,17,-1,17,17,17,17,17,-24,-26,17,-5,17,-23,-25,17,17,17,17,]),'LOG':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[18,18,18,-35,18,18,18,18,-34,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-14,18,-32,18,18,18,18,18,18,18,18,18,-20,-31,18,18,18,18,18,-18,-21,18,18,-3,18,18,18,18,18,18,-1,18,18,18,18,18,-24,-26,18,-5,18,-23,-25,18,18,18,18,]),'RAND':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[19,19,19,-35,19,19,19,19,-34,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-14,19,-32,19,19,19,19,19,19,19,19,19,-20,-31,19,19,19,19,19,-18,-21,19,19,-3,19,19,19,19,19,19,-1,19,19,19,19,19,-24,-26,19,-5,19,-23,-25,19,19,19,19,]),'PRINT':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[20,20,20,-35,20,20,20,20,-34,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-14,20,-32,20,20,20,20,20,20,20,20,20,-20,-31,20,20,20,20,20,-18,-21,20,20,-3,20,20,20,20,20,20,-1,20,20,20,20,20,-24,-26,20,-5,20,-23,-25,20,20,20,20,]),'NOT':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[21,21,21,-35,21,21,21,21,-34,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-14,21,-32,21,21,21,21,21,21,21,21,21,-20,-31,21,21,21,21,21,-18,-21,21,21,-3,21,21,21,21,21,21,-1,21,21,21,21,21,-24,-26,21,-5,21,-23,-25,21,21,21,21,]),'FUNCTION':([0,10,11,37,54,58,59,94,97,98,112,113,114,118,132,138,139,150,152,153,158,162,163,164,169,172,173,178,182,],[22,22,-35,-34,-14,22,-32,22,-20,-31,22,22,-18,-21,-3,22,22,22,22,-1,22,22,-24,-26,-5,-23,-25,22,22,]),'NUMBER':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,140,149,150,152,153,155,157,158,160,162,163,164,165,167,169,170,172,173,176,178,180,182,],[23,23,23,-35,23,23,23,23,-34,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-14,23,-32,23,23,23,23,23,23,23,23,23,-20,-31,23,23,23,23,23,-18,-21,23,23,-3,23,23,23,154,23,23,23,-1,23,23,23,23,23,-24,-26,174,23,-5,23,-23,-25,23,23,23,23,]),'PI':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[24,24,24,-35,24,24,24,24,-34,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-14,24,-32,24,24,24,24,24,24,24,24,24,-20,-31,24,24,24,24,24,-18,-21,24,24,-3,24,24,24,24,24,24,-1,24,24,24,24,24,-24,-26,24,-5,24,-23,-25,24,24,24,24,]),'E':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[25,25,25,-35,25,25,25,25,-34,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-14,25,-32,25,25,25,25,25,25,25,25,25,-20,-31,25,25,25,25,25,-18,-21,25,25,-3,25,25,25,25,25,25,-1,25,25,25,25,25,-24,-26,25,-5,25,-23,-25,25,25,25,25,]),'TRUE':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[26,26,26,-35,26,26,26,26,-34,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-14,26,-32,26,26,26,26,26,26,26,26,26,-20,-31,26,26,26,26,26,-18,-21,26,26,-3,26,26,26,26,26,26,-1,26,26,26,26,26,-24,-26,26,-5,26,-23,-25,26,26,26,26,]),'FALSE':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[27,27,27,-35,27,27,27,27,-34,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-14,27,-32,27,27,27,27,27,27,27,27,27,-20,-31,27,27,27,27,27,-18,-21,27,27,-3,27,27,27,27,27,27,-1,27,27,27,27,27,-24,-26,27,-5,27,-23,-25,27,27,27,27,]),'STRING':([0,3,10,11,21,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,61,62,63,64,66,71,94,96,97,98,106,109,111,112,113,114,118,123,129,132,137,138,139,149,150,152,153,155,157,158,160,162,163,164,167,169,170,172,173,176,178,180,182,],[28,28,28,-35,28,28,28,28,-34,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-14,28,-32,28,28,28,28,28,28,28,28,28,-20,-31,28,28,28,28,28,-18,-21,28,28,-3,28,28,28,28,28,28,-1,28,28,28,28,28,-24,-26,28,-5,28,-23,-25,28,28,28,28,]),'$end':([1,11,37,54,97,114,118,132,153,163,164,169,172,173,],[0,-35,-34,-14,-20,-18,-21,-3,-1,-24,-26,-5,-23,-25,]),'ASIGN2':([4,],[34,]),'SEMICOLON':([4,6,8,12,13,23,24,25,26,27,28,32,67,70,73,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,97,104,110,115,119,120,121,122,124,130,133,148,151,161,166,],[-50,37,54,-33,-36,-44,-45,-46,-47,-48,-49,-15,-66,-43,-13,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,-67,118,-56,-22,37,-51,-52,-53,-54,-57,-19,37,-55,163,172,-4,]),'PLUS':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,38,-15,-33,-36,-44,-45,-46,-47,-48,-49,38,-15,38,-43,-13,38,38,-37,-38,-39,-40,-41,-42,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-56,38,38,-22,38,38,-51,-52,-53,-54,-57,38,38,38,38,38,-55,38,38,38,38,38,38,38,38,38,]),'MINUS':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,39,-15,-33,-36,-44,-45,-46,-47,-48,-49,39,-15,39,-43,-13,39,39,-37,-38,-39,-40,-41,-42,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-56,39,39,-22,39,39,-51,-52,-53,-54,-57,39,39,39,39,39,-55,39,39,39,39,39,39,39,39,39,]),'TIMES':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,40,-15,-33,-36,-44,-45,-46,-47,-48,-49,40,-15,40,-43,-13,40,40,40,40,-39,-40,-41,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-56,40,40,-22,40,40,-51,-52,-53,-54,-57,40,40,40,40,40,-55,40,40,40,40,40,40,40,40,40,]),'DIVIDE':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,41,-15,-33,-36,-44,-45,-46,-47,-48,-49,41,-15,41,-43,-13,41,41,41,41,-39,-40,-41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-56,41,41,-22,41,41,-51,-52,-53,-54,-57,41,41,41,41,41,-55,41,41,41,41,41,41,41,41,41,]),'POW':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,42,-15,-33,-36,-44,-45,-46,-47,-48,-49,42,-15,42,-43,-13,42,42,42,42,-39,-40,-41,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-56,42,42,-22,42,42,-51,-52,-53,-54,-57,42,42,42,42,42,-55,42,42,42,42,42,42,42,42,42,]),'MOD':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,43,-15,-33,-36,-44,-45,-46,-47,-48,-49,43,-15,43,-43,-13,43,43,-37,-38,-39,-40,-41,-42,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-56,43,43,-22,43,43,-51,-52,-53,-54,-57,43,43,43,43,43,-55,43,43,43,43,43,43,43,43,43,]),'EQ':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,44,-15,-33,-36,-44,-45,-46,-47,-48,-49,44,-15,44,-43,-13,44,44,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,44,44,44,44,44,44,44,44,44,-56,44,44,-22,44,44,-51,-52,-53,-54,-57,44,44,44,44,44,-55,44,44,44,44,44,44,44,44,44,]),'GT':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,45,-15,-33,-36,-44,-45,-46,-47,-48,-49,45,-15,45,-43,-13,45,45,-37,-38,-39,-40,-41,-42,45,-59,-60,-61,-62,45,45,45,45,45,45,45,45,45,45,-56,45,45,-22,45,45,-51,-52,-53,-54,-57,45,45,45,45,45,-55,45,45,45,45,45,45,45,45,45,]),'LT':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,46,-15,-33,-36,-44,-45,-46,-47,-48,-49,46,-15,46,-43,-13,46,46,-37,-38,-39,-40,-41,-42,46,-59,-60,-61,-62,46,46,46,46,46,46,46,46,46,46,-56,46,46,-22,46,46,-51,-52,-53,-54,-57,46,46,46,46,46,-55,46,46,46,46,46,46,46,46,46,]),'GE':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,47,-15,-33,-36,-44,-45,-46,-47,-48,-49,47,-15,47,-43,-13,47,47,-37,-38,-39,-40,-41,-42,47,-59,-60,-61,-62,47,47,47,47,47,47,47,47,47,47,-56,47,47,-22,47,47,-51,-52,-53,-54,-57,47,47,47,47,47,-55,47,47,47,47,47,47,47,47,47,]),'LE':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,48,-15,-33,-36,-44,-45,-46,-47,-48,-49,48,-15,48,-43,-13,48,48,-37,-38,-39,-40,-41,-42,48,-59,-60,-61,-62,48,48,48,48,48,48,48,48,48,48,-56,48,48,-22,48,48,-51,-52,-53,-54,-57,48,48,48,48,48,-55,48,48,48,48,48,48,48,48,48,]),'NE':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,49,-15,-33,-36,-44,-45,-46,-47,-48,-49,49,-15,49,-43,-13,49,49,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,49,49,49,49,49,49,49,49,49,-56,49,49,-22,49,49,-51,-52,-53,-54,-57,49,49,49,49,49,-55,49,49,49,49,49,49,49,49,49,]),'AND':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,50,-15,-33,-36,-44,-45,-46,-47,-48,-49,50,-15,50,-43,-13,50,50,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,50,50,50,50,50,50,50,50,-56,50,50,-22,50,50,-51,-52,-53,-54,-57,50,50,50,50,50,-55,50,50,50,50,50,50,50,50,50,]),'OR':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,51,-15,-33,-36,-44,-45,-46,-47,-48,-49,51,-15,51,-43,-13,51,51,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,51,51,51,51,51,51,51,-56,51,51,-22,51,51,-51,-52,-53,-54,-57,51,51,51,51,51,-55,51,51,51,51,51,51,51,51,51,]),'CONCAT':([4,6,8,12,13,23,24,25,26,27,28,30,32,67,70,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,103,104,105,108,110,115,117,119,120,121,122,124,130,131,133,135,141,148,151,161,166,168,171,175,177,181,184,],[-50,52,-15,-33,-36,-44,-45,-46,-47,-48,-49,52,-15,52,-43,-13,52,52,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,52,52,52,52,52,52,52,-56,52,52,-22,52,52,-51,-52,-53,-54,-57,52,52,52,52,52,-55,52,52,52,52,52,52,52,52,52,]),'RPAREN':([4,12,13,23,24,25,26,27,28,30,32,35,65,67,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,101,102,104,105,106,108,110,119,120,121,122,124,125,127,130,131,135,148,166,168,171,174,175,177,179,],[-50,-33,-36,-44,-45,-46,-47,-48,-49,70,-15,-30,104,-66,-43,-13,110,-29,-28,112,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,-67,113,119,120,121,122,-56,124,126,129,-22,-51,-52,-53,-54,-57,136,139,-19,-27,148,-55,-4,176,178,179,180,182,-2,]),'COMA':([4,12,13,23,24,25,26,27,28,32,35,55,56,67,70,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,103,104,106,110,116,117,119,120,121,122,124,125,130,131,148,154,166,],[-50,-33,-36,-44,-45,-46,-47,-48,-49,-15,-30,95,-17,-66,-43,95,-13,111,-29,-28,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,-67,123,-56,-30,-22,-16,-12,-51,-52,-53,-54,-57,111,-19,-27,-55,165,-4,]),'ELIF':([4,8,11,12,13,23,24,25,26,27,28,32,37,54,67,70,73,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,97,104,110,114,115,118,119,120,121,122,124,130,132,133,134,141,142,143,145,146,148,153,163,164,166,169,172,173,181,183,184,185,],[-50,-15,-35,-33,-36,-44,-45,-46,-47,-48,-49,-15,-34,-14,-66,-43,-13,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,-67,-20,-56,-22,-18,-19,-21,-51,-52,-53,-54,-57,-19,-3,144,147,144,156,-9,159,-6,-55,-1,-24,-26,-4,-5,-23,-25,-10,-7,-11,-8,]),'ELSE':([4,8,11,12,13,23,24,25,26,27,28,32,37,54,67,70,73,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,97,104,110,114,115,118,119,120,121,122,124,130,132,133,134,141,142,143,145,146,148,153,163,164,166,169,172,173,181,183,184,185,],[-50,-15,-35,-33,-36,-44,-45,-46,-47,-48,-49,-15,-34,-14,-66,-43,-13,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,-67,-20,-56,-22,-18,-19,-21,-51,-52,-53,-54,-57,-19,-3,-30,-30,-30,155,-9,158,-6,-55,-1,-24,-26,-4,-5,-23,-25,-10,-7,-11,-8,]),'IN':([4,12,13,23,24,25,26,27,28,32,55,56,67,69,70,72,73,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,104,110,116,117,119,120,121,122,124,130,148,166,],[-50,-33,-36,-44,-45,-46,-47,-48,-49,-15,94,-17,-66,107,-43,109,-13,-37,-38,-39,-40,-41,-42,-58,-59,-60,-61,-62,-63,-64,-65,-67,-56,-22,-16,-12,-51,-52,-53,-54,-57,-19,-55,-4,]),'RBRACE':([11,37,54,58,59,97,98,114,118,132,152,153,162,163,164,169,172,173,],[-35,-34,-14,97,-32,-20,-31,-18,-21,-3,164,-1,173,-24,-26,-5,-23,-25,]),'ASIGN':([57,],[96,]),'RANGE':([107,],[128,]),'ARROW':([126,136,],[137,149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,10,58,94,112,113,138,139,150,152,158,162,178,182,],[1,59,98,114,132,134,59,153,59,98,169,98,183,185,]),'expression':([0,3,10,21,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,58,60,61,62,63,64,66,71,94,96,106,109,111,112,113,123,129,137,138,139,149,150,152,155,157,158,160,162,167,170,176,178,180,182,],[6,30,6,67,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,6,99,100,101,102,103,105,108,115,117,75,130,131,6,133,135,141,151,6,6,161,6,6,166,168,6,171,6,175,177,181,6,184,6,]),'asig2':([0,3,10,21,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,58,60,61,62,63,64,66,71,94,96,106,109,111,112,113,123,129,137,138,139,149,150,152,155,157,158,160,162,167,170,176,178,180,182,],[8,32,8,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,8,32,32,32,32,32,32,32,8,32,32,32,32,8,8,32,32,32,8,8,32,8,8,32,32,8,32,8,32,32,32,8,32,8,]),'functionDef':([0,10,58,94,112,113,138,139,150,152,158,162,178,182,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'function':([0,3,10,21,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,58,60,61,62,63,64,66,71,94,96,106,109,111,112,113,123,129,137,138,139,149,150,152,155,157,158,160,162,167,170,176,178,180,182,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'factor':([0,3,10,21,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,58,60,61,62,63,64,66,71,94,96,106,109,111,112,113,123,129,137,138,139,149,150,152,155,157,158,160,162,167,170,176,178,180,182,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'asigs':([9,33,],[55,72,]),'asig':([9,33,95,],[56,56,116,]),'statements':([10,138,150,],[58,152,162,]),'parameters':([35,106,],[74,125,]),'empty':([35,106,133,134,141,],[76,76,143,146,143,]),'iterable':([107,],[127,]),'elifsExp':([133,141,],[142,142,]),'elifs':([134,],[145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> FOR LPAREN ID IN iterable RPAREN statement','statement',7,'p_for','my_parser.py',35),
  ('iterable -> RANGE LPAREN NUMBER COMA NUMBER RPAREN','iterable',6,'p_iterable','my_parser.py',39),
  ('statement -> WHILE LPAREN expression RPAREN statement','statement',5,'p_while_statement','my_parser.py',43),
  ('expression -> IF LPAREN expression RPAREN expression elifsExp ELSE expression','expression',8,'p_conditions','my_parser.py',47),
  ('statement -> IF LPAREN expression RPAREN statement elifs ELSE statement','statement',8,'p_conditions_statement','my_parser.py',51),
  ('elifs -> empty','elifs',1,'p_condition_elif','my_parser.py',55),
  ('elifs -> ELIF LPAREN expression RPAREN statement','elifs',5,'p_condition_elif','my_parser.py',56),
  ('elifs -> elifs ELIF LPAREN expression RPAREN statement','elifs',6,'p_condition_elif','my_parser.py',57),
  ('elifsExp -> empty','elifsExp',1,'p_condition_elif_expression','my_parser.py',66),
  ('elifsExp -> ELIF LPAREN expression RPAREN expression','elifsExp',5,'p_condition_elif_expression','my_parser.py',67),
  ('elifsExp -> elifsExp ELIF LPAREN expression RPAREN expression','elifsExp',6,'p_condition_elif_expression','my_parser.py',68),
  ('asig -> ID ASIGN expression','asig',3,'p_asig','my_parser.py',77),
  ('asig2 -> ID ASIGN2 expression','asig2',3,'p_asig2','my_parser.py',81),
  ('statement -> asig2 SEMICOLON','statement',2,'p_asign2_statement','my_parser.py',85),
  ('expression -> asig2','expression',1,'p_asign2_expression','my_parser.py',89),
  ('asigs -> asigs COMA asig','asigs',3,'p_asigs','my_parser.py',93),
  ('asigs -> asig','asigs',1,'p_asigs','my_parser.py',94),
  ('statement -> LET asigs IN statement','statement',4,'p_multivariables','my_parser.py',101),
  ('expression -> LET asigs IN expression','expression',4,'p_multivariables_expression','my_parser.py',105),
  ('statement -> LBRACE statements RBRACE','statement',3,'p_expression_block','my_parser.py',110),
  ('statement -> LBRACE statements RBRACE SEMICOLON','statement',4,'p_expression_block','my_parser.py',111),
  ('function -> ID LPAREN parameters RPAREN','function',4,'p_expression_function','my_parser.py',116),
  ('functionDef -> FUNCTION ID LPAREN parameters RPAREN ARROW expression SEMICOLON','functionDef',8,'p_function_inline','my_parser.py',120),
  ('functionDef -> FUNCTION ID LPAREN RPAREN ARROW expression SEMICOLON','functionDef',7,'p_function_inline','my_parser.py',121),
  ('functionDef -> FUNCTION ID LPAREN parameters RPAREN LBRACE statements RBRACE','functionDef',8,'p_function_full','my_parser.py',128),
  ('functionDef -> FUNCTION ID LPAREN RPAREN LBRACE statements RBRACE','functionDef',7,'p_function_full','my_parser.py',129),
  ('parameters -> parameters COMA expression','parameters',3,'p_parameters','my_parser.py',137),
  ('parameters -> empty','parameters',1,'p_parameters','my_parser.py',138),
  ('parameters -> expression','parameters',1,'p_parameters_expression','my_parser.py',147),
  ('empty -> <empty>','empty',0,'p_empty','my_parser.py',151),
  ('statements -> statements statement','statements',2,'p_statements','my_parser.py',156),
  ('statements -> statement','statements',1,'p_statements','my_parser.py',157),
  ('expression -> function','expression',1,'p_function','my_parser.py',164),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','my_parser.py',168),
  ('statement -> functionDef','statement',1,'p_statement','my_parser.py',169),
  ('expression -> factor','expression',1,'p_expression','my_parser.py',173),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','my_parser.py',178),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','my_parser.py',179),
  ('expression -> expression TIMES expression','expression',3,'p_term_binop','my_parser.py',186),
  ('expression -> expression DIVIDE expression','expression',3,'p_term_binop','my_parser.py',187),
  ('expression -> expression POW expression','expression',3,'p_term_binop','my_parser.py',188),
  ('expression -> expression MOD expression','expression',3,'p_term_binop','my_parser.py',189),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_factor_group','my_parser.py',197),
  ('factor -> NUMBER','factor',1,'p_factor_num_const','my_parser.py',201),
  ('factor -> PI','factor',1,'p_factor_num_const','my_parser.py',202),
  ('factor -> E','factor',1,'p_factor_num_const','my_parser.py',203),
  ('factor -> TRUE','factor',1,'p_factor_num_const','my_parser.py',204),
  ('factor -> FALSE','factor',1,'p_factor_num_const','my_parser.py',205),
  ('factor -> STRING','factor',1,'p_factor_num_const','my_parser.py',206),
  ('factor -> ID','factor',1,'p_factor_num_const','my_parser.py',207),
  ('expression -> SIN LPAREN expression RPAREN','expression',4,'p_factor_func','my_parser.py',223),
  ('expression -> COS LPAREN expression RPAREN','expression',4,'p_factor_func','my_parser.py',224),
  ('expression -> SQRT LPAREN expression RPAREN','expression',4,'p_factor_func','my_parser.py',225),
  ('expression -> EXP LPAREN expression RPAREN','expression',4,'p_factor_func','my_parser.py',226),
  ('expression -> LOG LPAREN expression COMA expression RPAREN','expression',6,'p_factor_func','my_parser.py',227),
  ('expression -> RAND LPAREN RPAREN','expression',3,'p_factor_func','my_parser.py',228),
  ('expression -> PRINT LPAREN expression RPAREN','expression',4,'p_factor_func','my_parser.py',229),
  ('expression -> expression EQ expression','expression',3,'p_factor_binop','my_parser.py',239),
  ('expression -> expression GT expression','expression',3,'p_factor_binop','my_parser.py',240),
  ('expression -> expression LT expression','expression',3,'p_factor_binop','my_parser.py',241),
  ('expression -> expression GE expression','expression',3,'p_factor_binop','my_parser.py',242),
  ('expression -> expression LE expression','expression',3,'p_factor_binop','my_parser.py',243),
  ('expression -> expression NE expression','expression',3,'p_factor_binop','my_parser.py',244),
  ('expression -> expression AND expression','expression',3,'p_factor_logicop','my_parser.py',248),
  ('expression -> expression OR expression','expression',3,'p_factor_logicop','my_parser.py',249),
  ('expression -> NOT expression','expression',2,'p_factor_logineg','my_parser.py',253),
  ('expression -> expression CONCAT expression','expression',3,'p_factor_concat','my_parser.py',258),
]
