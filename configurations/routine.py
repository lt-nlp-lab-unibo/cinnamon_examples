from cinnamon_core.core.registry import Registry, RegistrationKey, register
from cinnamon_generic.components.routine import TrainAndTestRoutine
from cinnamon_generic.configurations.routine import RoutineConfig


class ExampleRoutineConfig(RoutineConfig):

    @classmethod
    def get_default(
            cls
    ):
        config = super().get_default()

        config.data_loader = RegistrationKey(name='data_loader',
                                             tags={'imdb', 'default'},
                                             namespace='examples')
        config.pre_processor = RegistrationKey(name='processor',
                                               tags={'tf-idf', 'label', 'ml'},
                                               namespace='examples')
        config.data_splitter = RegistrationKey(name='data_splitter',
                                               tags={'sklearn', 'tt'},
                                               namespace='generic')
        config.model = RegistrationKey(name='model',
                                       tags={'svm', 'default'},
                                       namespace='examples')
        config.metrics = RegistrationKey(name='metrics',
                                         tags={'binary_f1', 'macro_f1', 'accuracy'},
                                         namespace='examples')
        config.helper = RegistrationKey(name='helper',
                                        tags={'default'},
                                        namespace='generic')
        config.routine_processor = RegistrationKey(name='routine_processor',
                                                   tags={'average'},
                                                   namespace='generic')

        config.seeds = [15000, 42]

        return config


@register
def register_routines():
    Registry.add_and_bind(config_class=ExampleRoutineConfig,
                          component_class=TrainAndTestRoutine,
                          name='routine',
                          tags={'train_and_test'},
                          namespace='examples')
