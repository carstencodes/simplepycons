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


class PixabayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pixabay"

    @property
    def original_file_name(self) -> "str":
        return "pixabay.svg"

    @property
    def title(self) -> "str":
        return "Pixabay"

    @property
    def primary_color(self) -> "str":
        return "#2EC66D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pixabay</title>
     <path d="M5.627 10.234a.888.888 0 01-.887-.888H1.7c0
 .49-.398.888-.888.888H0v9.447h15.56v-9.447H5.64zm-.886
 2.796h-3.04v-1.323h3.04v1.323zm5.344 5.234a3.271 3.271 0
 01-3.267-3.269c0-1.802 1.466-3.193 3.267-3.193s3.267 1.39 3.267
 3.193a3.271 3.271 0 01-3.267 3.269zm1.756-3.269c0 .969-.788
 1.757-1.756 1.757a1.759 1.759 0 01-1.756-1.757c0-.969.788-1.757
 1.756-1.757s1.756.788 1.756 1.757zM24 9.501l-3.93
 10.156-3.164-1.226V16.7l2.242.869 2.765-7.146L11.55 6.407l-.96
 2.482h-1.73l1.769-4.57L24 9.501Z" />
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
