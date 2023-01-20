# sc-feature-module-cookie

[CookieCutter](https://github.com/cookiecutter/cookiecutter) template for sharechat android feature module

## Usage

1. Install the latest CookieCutter
    ```
    pip install -U cookiecutter
    ```
1. Generate android module using the template
    ```
    cookiecutter https://github.com/Kshitij09-sc/sc-feature-module-cookie.git
    ```
1. Enter module name & package name as per given format
1. CookieCutter will generate required module files and update `settings.gradle.kts` with given module name if file exists


## Example Directory Structure

_Example directory structure for module name `:feature:awesome` and package name `sharechat.feature.awesome`_
```
feature
└── awesome
    ├── build.gradle.kts
    ├── consumer-rules.pro
    ├── proguard-rules.pro
    └── src
        ├── androidTest
        │   └── java
        │       └── sharechat
        │           └── feature
        │               └── awesome
        │                   └── ExampleInstrumentedTest.kt
        ├── main
        │   ├── AndroidManifest.xml
        │   └── java
        │       └── sharechat
        │           └── feature
        │               └── awesome
        └── test
            └── java
                └── sharechat
                    └── feature
                        └── awesome
                            └── ExampleUnitTest.kt
```