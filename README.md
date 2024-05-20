# KubeDraw

KubeDraw is a Python-based tool designed to simplify the visualization of Kubernetes infrastructure. With its straightforward command-line interface, KubeDraw allows users to quickly generate detailed diagrams of their Kubernetes cluster architecture.

## Requirements

To use KubeDraw, you'll need to install the following dependencies:

- **`kubernetes`**: Python client for Kubernetes. You can install it via pip:

```bash
pip install kubernetes
```

- **`graphviz`**: Graph visualization software. You can install it via pip:

```bash
pip install graphviz
```

- **`diagrams`**: Python library for creating diagrams. You can install it via pip:

```bash
pip install diagrams
```

## Usage

To generate a visual diagram of your Kubernetes cluster, simply run:

```bash
git clone https://github.com/B0nam/kubedraw.git
python /src/kubedraw
```

This will create a visual representation of all namespaces.

You can specify a namespace by using:

```bash
git clone https://github.com/B0nam/kubedraw.git
python /src/kubedraw your-namespace
```

## Exemple

Here's a basic example of a KubeDraw diagram:
![namespace:_default](https://github.com/B0nam/kubedraw/assets/85623265/7fbc4656-9a13-4672-bf07-98ee7235c72a)


## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
