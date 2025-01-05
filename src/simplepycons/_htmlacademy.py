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


class HtmlAcademyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "htmlacademy"

    @property
    def original_file_name(self) -> "str":
        return "htmlacademy.svg"

    @property
    def title(self) -> "str":
        return "HTML Academy"

    @property
    def primary_color(self) -> "str":
        return "#302683"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HTML Academy</title>
     <path d="M12 0L2.524.994v17.368L12 24l9.476-5.638V.994L12.099.01
 12 0zm8.236 17.657L12 22.557l-8.236-4.9v-7.119l8.2
 4.881.014.885-5.626-3.349-.008.86 5.648
 3.394.015.908-5.647-3.36-.008.86L12
 19.01l5.703-3.412v-.862l-.008.004v-2.805l2.54-1.517v7.238zm-.006-8.162l-2.254
 1.328-1.04.613-4.96-2.951-.009.858 4.24
 2.521-.037.023-.092.054-.602.355-3.5-2.083-.009.859 2.763
 1.643-.652.436-.015.01-2.088-1.23-.008.858
 1.37.807-1.395.837-8.16-4.85 8.172-4.912v.001l8.276
 4.823zm.006-.864l-8.28-4.882h-.002l-8.19 4.877V2.11L12
 1.246l8.237.864v6.52z" />
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
