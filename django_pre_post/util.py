def AnswerDisplay(self, obj):
    type = obj.get_type_display()
    if type == 'Multiple Choice':
        return obj.get_expectedMultipleChoiceAnswer_display()
    elif type == 'Numeric' or type == 'Rank':
        return str(obj.expectedNumericAnswer)
    elif type == 'Info':
        return ''
    else:
        return obj.expectedTextAnswer


class TemplateBoolean():
    value = False

    def false(self):
        self.value = False
        return ''

    def true(self):
        self.value = True
        return ''
