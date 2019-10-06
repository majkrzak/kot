from lxml import etree


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
            with open(f'{mod}/{self.name}.{mod}.iml', 'wb') as f:
                f.write(etree.tostring(self.build_module(mod), pretty_print=True))
        with open(f'{self.name}.ipr', 'wb') as f:
            f.write(etree.tostring(self.build_project(), pretty_print=True))

    def build_module(self, mod):
        module = etree.Element('module', type="JAVA_MODULE", version="4")
        component = etree.SubElement(module, 'component', {
            'name': 'NewModuleRootManager',
            'inherit-compiler-output': 'true'
        })
        etree.SubElement(component, 'exclude-output')
        content = etree.SubElement(component, 'content', {'url': 'file://$MODULE_DIR$'})
        etree.SubElement(content, 'sourceFolder', {'url': 'file://$MODULE_DIR$', 'isTestSource': 'false'})
        etree.SubElement(component, 'orderEntry', {'type': 'inheritedJdk'})
        etree.SubElement(component, 'orderEntry', {'type': 'sourceFolder', 'forTests': 'false'})
        for dep in self.mods[mod]:
            etree.SubElement(component, 'orderEntry', {'type': 'module', 'module-name': f'{self.name}.{dep}'})
        for lib in self.libs.keys():
            etree.SubElement(component, 'orderEntry', {'type': 'library', 'name': lib, 'level': 'project'})
        return module

    def build_project(self):
        project = etree.Element('project', version="4")
        component_mm = etree.SubElement(project, 'component', {'name': 'ProjectModuleManager'})
        modules = etree.SubElement(component_mm, 'modules')
        for mod in self.mods:
            etree.SubElement(modules, 'module', {
                'fileurl': f'file://$PROJECT_DIR$/{mod}/{self.name}.{mod}.iml',
                'filepath': f'$PROJECT_DIR$/{mod}/{self.name}.{mod}.iml'
            })
        component_rm = etree.SubElement(project, 'component', {
            'name': 'ProjectRootManager',
            'version': "2",
            'languageLevel': "JDK_1_9",
            'default': "false",
            'project-jdk-name': "11",
            'project-jdk-type': "JavaSDK"
        })
        etree.SubElement(component_rm, 'output', {'url': 'file://$PROJECT_DIR$/out'})
        component_lt = etree.SubElement(project, 'component', {'name': 'libraryTable'})
        for lib in self.libs.keys():
            library = etree.SubElement(component_lt, 'library', {'name': lib})
            classes = etree.SubElement(library, 'CLASSES')
            for res in self.libs[lib]:
                etree.SubElement(classes, 'root', {'url': f'jar://$PROJECT_DIR$/.lib/{res}.jar!/'})
            etree.SubElement(library, 'JAVADOC')
            etree.SubElement(library, 'SOURCES')
        return project
