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


class GreatLearningIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "greatlearning"

    @property
    def original_file_name(self) -> "str":
        return "greatlearning.svg"

    @property
    def title(self) -> "str":
        return "Great Learning"

    @property
    def primary_color(self) -> "str":
        return "#0E39A9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Great Learning</title>
     <path d="M14.373 0c-6.617 0-12 5.383-12 12s5.383 12 12
 12h.856c.958-1.175 1.911-2.354 2.867-3.531h-3.723c-4.669
 0-8.469-3.8-8.469-8.469 0-4.67 3.8-8.469 8.469-8.469h4.375L21.615
 0Zm3.723 20.469 3.531-4.354v-6.013h-7.502l-2.861 3.533h6.832z" />
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
