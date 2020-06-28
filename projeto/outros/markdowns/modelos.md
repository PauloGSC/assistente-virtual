## Modelos

Lista de modelos/exemplos que podem ser usados como base para a construção da rede neural do projeto.

Os modelos devem estar escritos em PyTorch, ser da versão 3, 4 ou 5 do YOLO e suportarem customização mínima.

#### Explicação

![Modelo](../../.assets/modelo.png)

Um modelo, em Deep Learning, é uma combinação de Arquitetura + Pesos.

A Arquitetura representa os hiperparâmetros da rede (camadas, funções de ativação, função de perda, número de neurônios, taxa de aprendizado, etc).

Os Pesos são os reais parâmetros da rede, as conexões entre as camadas (aquilo que a rede aprende durante o treinamento).

#### Lista

| Repositório | Custom data | Finetuning |
|:-----------:|:-----------:|:----------:|
| [YoloV3-Custom-Object-Detection][0] | Ótimo | Bom |
| [YOLOv3_PyTorch][1] | Ruim | Bom |
| [YOLOv3-in-PyTorch][2] | Bom | Bom |
| [PyTorch-YOLOv3][3] | Bom | Ruim |
| [pytorch-yolo-v3-custom][4] | Ótimo | Ótimo |
| [yolov3][5] | Ótimo | ? |
| [yolov5][6] | Ótimo | ? |

* [yolov5][6] está disponível no PyTorch [Hub](https://pytorch.org/docs/stable/hub.html), conforme as [instruções](https://github.com/ultralytics/yolov5/issues/36)

[0]: https://github.com/TheCaffeineDev/YoloV3-Custom-Object-Detection
[1]: https://github.com/BobLiu20/YOLOv3_PyTorch
[2]: https://github.com/westerndigitalcorporation/YOLOv3-in-PyTorch
[3]: https://github.com/eriklindernoren/PyTorch-YOLOv3
[4]: https://github.com/michhar/pytorch-yolo-v3-custom
[5]: https://github.com/ultralytics/yolov3
[6]: https://github.com/ultralytics/yolov5
