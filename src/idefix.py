from lxml.etree import (
    tostring,
    Element,
    SubElement,
)


class Idefix:
    name: str
    libs: dict
    mods: dict

    def __init__(self, name, libs, mods):
        self.name = name
        self.libs = libs
        self.mods = mods

    def __call__(self):
        for mod in self.mods:
            iml = f'{mod}/{self.name}.{mod}.iml'

            with open(iml, 'wb') as f:
                self.write_xml_to_file(f, self.build_module(mod))

        with open(f'{self.name}.ipr', 'wb') as f:
            self.write_xml_to_file(f, self.build_project())

    def write_xml_to_file(self, f, xml):
        f.write(tostring(xml, pretty_print=True))

    def build_module(self, mod):
        module = Element('module', type="JAVA_MODULE", version="4")
        component = SubElement(module, 'component', {
            'name': 'NewModuleRootManager',
            'inherit-compiler-output': 'true'
        })
        SubElement(component, 'exclude-output')
        content = SubElement(component, 'content', {'url': 'file://$MODULE_DIR$'})
        SubElement(content, 'sourceFolder', {'url': 'file://$MODULE_DIR$', 'isTestSource': 'false'})
        SubElement(component, 'orderEntry', {'type': 'inheritedJdk'})
        SubElement(component, 'orderEntry', {'type': 'sourceFolder', 'forTests': 'false'})

        for dep in self.mods[mod]:
            SubElement(component, 'orderEntry', {'type': 'module', 'module-name': f'{self.name}.{dep}'})
        for lib in self.libs.keys():
            SubElement(component, 'orderEntry', {'type': 'library', 'name': lib, 'level': 'project'})
        return module

    def build_project(self):
        project = Element('project', version="4")
        component_mm = SubElement(project, 'component', {'name': 'ProjectModuleManager'})
        modules = SubElement(component_mm, 'modules')
        for mod in self.mods:
            SubElement(modules, 'module', {
                'fileurl': f'file://$PROJECT_DIR$/{mod}/{self.name}.{mod}.iml',
                'filepath': f'$PROJECT_DIR$/{mod}/{self.name}.{mod}.iml'
            })
        component_rm = SubElement(project, 'component', {
            'name': 'ProjectRootManager',
            'version': "2",
            'languageLevel': "JDK_1_9",
            'default': "false",
            'project-jdk-name': "11",
            'project-jdk-type': "JavaSDK"
        })
        SubElement(component_rm, 'output', {'url': 'file://$PROJECT_DIR$/out'})
        component_lt = SubElement(project, 'component', {'name': 'libraryTable'})
        for lib in self.libs.keys():
            library = SubElement(component_lt, 'library', {'name': lib})
            classes = SubElement(library, 'CLASSES')
            for res in self.libs[lib]:
                SubElement(classes, 'root', {'url': f'jar://$PROJECT_DIR$/.lib/{res.replace(":", "_")}.jar!/'})
            SubElement(library, 'JAVADOC')
            SubElement(library, 'SOURCES')

        return project
