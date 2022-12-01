# Rc-tasks

> A tool to fetch missing tasks for any language from Rosetta Code

[Read Author Notes to more information](#author-notes)

## Usage
```shell
$ rc-tasks
Type your language: Arturo
...
```

## Installing

For the latest version, please use:

```shell
pipx install $(
    curl 'https://api.github.com/repos/RickBarretto/rc-tasks/releases/latest' -s |
    grep 'browser_download_url' |
    cut -d ':' -f2,3 |
    cut -d '"' -f2 )
```

If you want to use another version, you have two options:
1. Use the install instruction from [Releases Tab][Releases]
2. Manually download, build and install

> Note: For the first, you'll need `pipx`,
> while for the second, you'll need `Poetry`

## Cheking
```shell
$ which rc-tasks
# or
$ where rc-tasks
```

## Manual Use

Clone the repository on your local machine

```shell
$ git clone https://github.com/RickBarretto/rc-tasks.git
```

### Running Locally (Without installing)

```shell
$ poetry update
$ poetry run rc-tasks
```

### Installing Locally

Using Poetry:

```shell
$ poetry shell
$ poetry install
```

> Note: Using `poetry install` just allow you to use
> on the current directory.
> But, it permits you to use without `poetry run` command
> while in `poetry shell` at least.


Using Pipx:

```shell
$ poetry build
$ pipx install ./dist/rc_tasks<TAB>
```

> Note: `<TAB>` indicates autocompletion.
> It's not a part of the command arguent.

---

## Author Notes

You can relate an Issue, if you found one
or if you have doubt about something.

### Installing Poetry and pipx

In this case, Poetry is optional.
Unless you want to build and install manually.

See [How to install Poetry][Poetry Installation]

While `pipx` is the tool used to actually install this app.

See [How to install pipx][pipx Installation]

### Where is pip?

So, as you can see, `pip` isn't used in this Project,
it's because it isn't the best tool for dependency management.
Really, I recomend you to use `pipx` for tools and applications
and `Poetry` for libraries and as your dependency manager.

Also, you can use `pip`, if you want.
Just replace from same command as [`pipx install`](#installing)
by using `pip` instead of `pipx`.

But you must to know, `pip` will install `requests-html`
at global scope. And not only application scope.
What can do conflicts with another projects. So be careful.

Read more about [Dependency Conflicts][pip #7744].

### Why not in PyPI

To avoids Typosquatting attacks, this tool isn't avaliable in PyPI,
so you must to open the github and copy the link on your terminal
instead just write the tool's name.

Read more about security in
[PyPI security pitfalls and steps towards
a secure Python ecosystem (2021)][Crane, 2021]
and
[The security risks of pip and PyPI (2020)][Garcia-Cabot, 2020]


[Releases]: https://github.com/RickBarretto/rc-tasks/releases/
[Poetry Installation]: https://python-poetry.org/docs/#installation
[pipx Installation]: https://pypa.github.io/pipx/installation/
[pip #7744]: https://github.com/pypa/pip/issues/7744
[Crane, 2021]: https://www.activestate.com/blog/pypi-security-pitfalls-and-steps-towards-a-secure-python-ecosystem/
[Garcia-Cabot, 2020]: https://carles-garcia.net/python/python_pip/