{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMD0q2gvM2vhWr3CtecgAo1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Zijun9/Awesome-LLM-Safety/blob/main/squares.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "h5Wbyk5aXQNl"
      },
      "outputs": [],
      "source": [
        "import numpy\n",
        "import torch\n",
        "## You only need to complete the two functions.\n",
        "def numpy_squares(k):\n",
        "  \"\"\"return (1, 4, 9, ..., k^2) as a numpy array\"\"\"\n",
        "  # your code here\n",
        "  return numpy.arange(1,k+1)**2\n",
        "\n",
        "\n",
        "\n",
        "def torch_squares(k):\n",
        "  \"\"\"return (1, 4, 9, ..., k^2) as a torch array\"\"\"\n",
        "  # your code here\n",
        "  return torch.arange(1,k+1)**2"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numpy_squares(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rBIuDc-2YItd",
        "outputId": "80825189-2fc3-4c0b-95ab-fbfad06b0996"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 1,  4,  9, 16, 25])"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "torch_squares(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2U2YqbX9YMCi",
        "outputId": "bb74f1c7-bb7c-4537-cff4-8b73274de122"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([ 1,  4,  9, 16, 25])"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "IKOrXanSYR73"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}