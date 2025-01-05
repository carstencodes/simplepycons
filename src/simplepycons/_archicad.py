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


class ArchicadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "archicad"

    @property
    def original_file_name(self) -> "str":
        return "archicad.svg"

    @property
    def title(self) -> "str":
        return "Archicad"

    @property
    def primary_color(self) -> "str":
        return "#2D50A5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Archicad</title>
     <path d="M22.5896 16.3222c-.779 0-1.4104-.6315-1.4104-1.4105
 0-.779.6314-1.4104 1.4104-1.4104S24 14.1328 24 14.9117c0 .779-.6315
 1.4105-1.4104 1.4105zM.1507 19.8272c-.35.6959-.0696 1.5438.6263
 1.8938.6959.35 1.5438.0695 1.8938-.6263 0 0 7.8494-16.0114
 14.2545-16.1487 4.2299-.0907 4.2313 5.642 4.2313 5.642 0 .779.6314
 1.4104 1.4104 1.4104s1.4104-.6314 1.4104-1.4104c0 0
 .0566-8.3813-7.0196-8.4569C8.7634 1.8711.1507 19.8272.1507 19.8272z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://graphisoft.com/contact-us/press-relat'''

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
