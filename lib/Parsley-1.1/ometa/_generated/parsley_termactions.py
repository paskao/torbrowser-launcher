def createParserClass(GrammarBase, ruleGlobals):
    if ruleGlobals is None:
        ruleGlobals = {}
    class parsley_termactions(GrammarBase):
        def rule_ruleValue(self):
            _locals = {'self': self}
            self.locals['ruleValue'] = _locals
            _G_apply_1, lastError = self._apply(self.rule_ws, "ws", [])
            self.considerError(lastError, 'ruleValue')
            _G_exactly_2, lastError = self.exactly('->')
            self.considerError(lastError, 'ruleValue')
            _G_apply_3, lastError = self._apply(self.rule_term, "term", [])
            self.considerError(lastError, 'ruleValue')
            _locals['tt'] = _G_apply_3
            _G_python_4, lastError = eval('t.Action(tt)', self.globals, _locals), None
            self.considerError(lastError, 'ruleValue')
            return (_G_python_4, self.currentError)


        def rule_semanticPredicate(self):
            _locals = {'self': self}
            self.locals['semanticPredicate'] = _locals
            _G_apply_5, lastError = self._apply(self.rule_ws, "ws", [])
            self.considerError(lastError, 'semanticPredicate')
            _G_exactly_6, lastError = self.exactly('?(')
            self.considerError(lastError, 'semanticPredicate')
            _G_apply_7, lastError = self._apply(self.rule_term, "term", [])
            self.considerError(lastError, 'semanticPredicate')
            _locals['tt'] = _G_apply_7
            _G_apply_8, lastError = self._apply(self.rule_ws, "ws", [])
            self.considerError(lastError, 'semanticPredicate')
            _G_exactly_9, lastError = self.exactly(')')
            self.considerError(lastError, 'semanticPredicate')
            _G_python_10, lastError = eval('t.Predicate(tt)', self.globals, _locals), None
            self.considerError(lastError, 'semanticPredicate')
            return (_G_python_10, self.currentError)


        def rule_semanticAction(self):
            _locals = {'self': self}
            self.locals['semanticAction'] = _locals
            _G_apply_11, lastError = self._apply(self.rule_ws, "ws", [])
            self.considerError(lastError, 'semanticAction')
            _G_exactly_12, lastError = self.exactly('!(')
            self.considerError(lastError, 'semanticAction')
            _G_apply_13, lastError = self._apply(self.rule_term, "term", [])
            self.considerError(lastError, 'semanticAction')
            _locals['tt'] = _G_apply_13
            _G_apply_14, lastError = self._apply(self.rule_ws, "ws", [])
            self.considerError(lastError, 'semanticAction')
            _G_exactly_15, lastError = self.exactly(')')
            self.considerError(lastError, 'semanticAction')
            _G_python_16, lastError = eval('t.Action(tt)', self.globals, _locals), None
            self.considerError(lastError, 'semanticAction')
            return (_G_python_16, self.currentError)


        def rule_application(self):
            _locals = {'self': self}
            self.locals['application'] = _locals
            def _G_optional_17():
                _G_apply_18, lastError = self._apply(self.rule_indentation, "indentation", [])
                self.considerError(lastError, None)
                return (_G_apply_18, self.currentError)
            def _G_optional_19():
                return (None, self.input.nullError())
            _G_or_20, lastError = self._or([_G_optional_17, _G_optional_19])
            self.considerError(lastError, 'application')
            _G_apply_21, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError, 'application')
            _locals['name'] = _G_apply_21
            def _G_or_22():
                _G_exactly_23, lastError = self.exactly('(')
                self.considerError(lastError, None)
                _G_apply_24, lastError = self._apply(self.rule_term_arglist, "term_arglist", [])
                self.considerError(lastError, None)
                _locals['args'] = _G_apply_24
                _G_exactly_25, lastError = self.exactly(')')
                self.considerError(lastError, None)
                _G_python_26, lastError = eval('t.Apply(name, self.rulename, args)', self.globals, _locals), None
                self.considerError(lastError, None)
                return (_G_python_26, self.currentError)
            def _G_or_27():
                _G_python_28, lastError = eval('t.Apply(name, self.rulename, [])', self.globals, _locals), None
                self.considerError(lastError, None)
                return (_G_python_28, self.currentError)
            _G_or_29, lastError = self._or([_G_or_22, _G_or_27])
            self.considerError(lastError, 'application')
            return (_G_or_29, self.currentError)


    if parsley_termactions.globals is not None:
        parsley_termactions.globals = parsley_termactions.globals.copy()
        parsley_termactions.globals.update(ruleGlobals)
    else:
        parsley_termactions.globals = ruleGlobals
    return parsley_termactions