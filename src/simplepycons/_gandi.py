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


class GandiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gandi"

    @property
    def original_file_name(self) -> "str":
        return "gandi.svg"

    @property
    def title(self) -> "str":
        return "Gandi"

    @property
    def primary_color(self) -> "str":
        return "#6640FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gandi</title>
     <path d="M16.72 5.908a1.496 1.496 0 1 1 2.442 1.729c-.871
 1.23-1.906 2.176-3.082 2.82-.661.436-1.414.844-2.209
 1.274-.689.373-1.401.758-2.065 1.171-1.565.974-2.46 1.87-2.814
 2.82-.473 1.266-.26 2.322.002 2.985a3.8 3.8 0 0 0 1.79 2.006c.808.413
 1.931.39 2.93-.06.924-.415 1.542-1.11
 1.612-1.813.07-.71-.24-1.114-.553-1.255-.368-.165-.788.006-1.152.467a1.495
 1.495 0 1 1-2.349-1.854c1.227-1.554 3.082-2.08 4.726-1.342 1.588.713
 2.493 2.392 2.305 4.28-.179 1.792-1.435 3.38-3.36
 4.246-1.836.826-3.899.824-5.52-.005a6.8 6.8 0 0
 1-3.212-3.572c-.642-1.625-.65-3.446-.022-5.13.605-1.62 1.869-2.803
 3.037-3.647a8 8 0 0
 1-.828-.33c-1.376-.638-2.573-1.668-3.56-3.061A1.496 1.496 0 0 1 7.28
 5.908c.69.976 1.467 1.654 2.376 2.075.69.319 1.457.487
 2.344.514.888-.027 1.656-.195
 2.345-.514q.098-.045.194-.096.106-.053.208-.112c.738-.424 1.387-1.038
 1.972-1.867M11.2 4.17c.191.192.447.297.717.297.271 0
 .526-.105.718-.297s.297-.446.297-.717a1 1 0 0 0-.298-.718 1 1 0 0
 0-.717-.297c-.27 0-.526.105-.717.297a1 1 0 0 0-.297.718c0
 .27.105.525.297.717M9.476 1.011A3.43 3.43 0 0 1 11.917 0c.922 0
 1.79.359 2.442 1.01a3.43 3.43 0 0 1 1.01 2.443c0 .922-.358 1.789-1.01
 2.44a3.43 3.43 0 0 1-2.442 1.012 3.43 3.43 0 0 1-2.44-1.011 3.43 3.43
 0 0 1-1.013-2.441c0-.923.36-1.79 1.012-2.442" />
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
