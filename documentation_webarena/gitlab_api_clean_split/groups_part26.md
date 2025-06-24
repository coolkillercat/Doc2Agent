## Namespaces in groups

By default, groups only get 20 namespaces at a time because the API results are paginated.

To get more (up to 100), pass the following as an argument to the API call:

```plaintext
/groups?per_page=100
```

And to switch pages add:

```plaintext
/groups?per_page=100&page=2
```

