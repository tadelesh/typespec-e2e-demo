// Code generated by Microsoft (R) TypeSpec Code Generator.

module todo {
    requires transitive io.clientcore.core;

    exports todo;
    exports todo.models;
    exports todo.todoitems.models;

    opens todo.implementation.models to io.clientcore.core;
    opens todo.models to io.clientcore.core;
    opens todo.todoitems.models to io.clientcore.core;
}
