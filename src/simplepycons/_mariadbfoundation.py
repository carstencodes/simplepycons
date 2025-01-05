#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class MariadbFoundationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mariadbfoundation"

    @property
    def original_file_name(self) -> "str":
        return "mariadbfoundation.svg"

    @property
    def title(self) -> "str":
        return "MariaDB Foundation"

    @property
    def primary_color(self) -> "str":
        return "#1F305F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MariaDB Foundation</title>
     <path d="M23.475
 4.031c-.369.013-.262.179-1.06.376-.805.198-1.78.077-2.646.441-2.267.95-2.634
 4.624-5.335 6.045-1.77 1-3.576 1.229-5.19
 1.735-1.295.52-2.101.864-3.051 1.683-.737.635-.917 1.252-1.687
 2.05-.782 1.062-3.744.118-4.506 1.45.402.26.634.332
 1.34.24-.146.276-1.074.64-.906 1.048 0 0 2.245.409
 4.137-.733.882-.359 1.71-1.119 3.08-1.301 1.777-.236 3.778.373
 5.925.544-.444.877-.902 1.395-1.391
 2.119-.152.163.13.307.65.209.937-.232 1.615-.483 2.289-.949.878-.606
 1.256-1.16 1.997-2.039.644 1.032 2.914 1.26
 3.38.367-.867-.367-1.052-2.277-.755-3.101.35-.786.603-1.896.886-2.928.256-.93.413-2.349.718-3.075.365-.903
 1.073-1.185 1.605-1.664.532-.479 1.06-.878
 1.045-1.974-.006-.356-.19-.553-.525-.543zm-.573.445c.09.307.231.448.841.504-.089.774-.606
 1.196-1.183 1.602-.509.356-1.066.7-1.424 1.258-.367.57-.951 2.23-1.52
 4.159-.492 1.668-1.065 2.807-2.276
 3.807-.15-.36.17-.568.03-.897-.175.496-.558 1.218-.789 1.66-.76
 1.454-2.019 2.63-3.901 2.962.893-1.21 1.787-2.543
 1.896-4.627-.4.087-.432 1.164-1.078
 1.56-.415.045-.995-.05-1.573-.12-1.726-.203-3.465-.282-5.087.24-1.105.353-2.356
 1.447-3.292 1.853-1.1.478-1.477.515-2.869.473-.174-.234
 1.002-.536.936-1.047-.536-.058-.848.071-1.314-.14a.707.707 0
 01.223-.24c.854-.59 3.278-.14
 3.927-.777.401-.392.663-.804.935-1.204.265-.388.538-.765.953-1.105.154-.125.394-.341.571-.463.709-.484
 1.51-.831 2.373-1.133 1.174-.413 2.361-.552 3.613-1.03.774-.296
 1.508-.576 2.193-1.088.162-.121.407-.326.55-.465 2.22-2.192
 2.361-5.177
 5.415-5.49.37-.038.672-.026.948-.034.317-.01.597-.047.902-.218zm-.15.197c-.017
 0-.049.015-.093.056-.265.272-.79.884-.98
 1.454-.05.155.048.11.082.01.189-.584.788-1.226.971-1.42.045-.052.051-.099.02-.1zm.08.133c-.017.002-.046.022-.084.069-.224.306-.657.77-.766
 1.36-.027.16.064.103.082-.001.106-.605.608-1.11.763-1.327.037-.058.036-.105.006-.101zm.098.12c-.017.004-.044.026-.077.076-.199.325-.46.699-.519
 1.295-.013.162.073.097.083-.008.052-.612.379-1.032.515-1.262.032-.06.028-.107-.002-.1zm.107.091c-.018.005-.042.03-.071.082-.169.34-.328.6-.334
 1.2.002.163.08.09.081-.015
 0-.614.22-.925.335-1.166.026-.063.018-.11-.011-.1zm-2.064.294c-.526.013-.837.242-.938.68.432.375
 1.338.074 1.177-.672a2.218 2.218 0 00-.24-.008Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
