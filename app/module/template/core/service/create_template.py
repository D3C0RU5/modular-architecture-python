from template.http.rest.dto.create_template import CreateTemplateRequestDTO


class TemplateService:
    def create(self, template: ):
        return {
            "name": template.name,
            "content": template.content,
        }
