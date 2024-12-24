#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class NintendoDsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nintendods"

    @property
    def original_file_name(self) -> "str":
        return "nintendods.svg"

    @property
    def title(self) -> "str":
        return "Nintendo DS"

    @property
    def primary_color(self) -> "str":
        return "#929497"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nintendo DS</title>
     <path d="M.286 10.773v1.142H0v-1.541h.244l1.155
 1.123v-1.123h.282v1.541h-.223zm2.86 0v1.142h-.285v-1.541h.244l1.155
 1.123v-1.123h.282v1.541h-.223zm5.93 0v1.142h-.285v-1.541h.243l1.156
 1.123v-1.123h.282v1.541h-.223zm-6.948-.399h.286v1.541h-.286zm2.738
 0h1.672v.265H5.85v1.276h-.297v-1.276h-.687zm1.996
 0h1.505v.265H7.144v.346h.946v.265h-.946v.4h1.223v.265H6.862zm5.665.225c.104.137.159.326.159.545
 0
 .221-.055.409-.159.546-.112.147-.277.225-.477.225h-1.143v-1.541h1.143c.2
 0 .365.078.477.225m-.469 1.051c.275 0 .372-.273.372-.506
 0-.232-.097-.505-.372-.505h-.876v1.011zm2.494-1.276c.18 0
 .327.147.327.327v.887c0 .18-.147.327-.327.327h-1.244a.327.327 0 0
 1-.326-.327v-.887c0-.18.146-.327.326-.327zm.053
 1.213v-.884c0-.035-.029-.064-.064-.064h-1.222c-.035
 0-.064.029-.064.064v.884c0 .034.029.063.064.063h1.222c.035 0
 .064-.029.064-.063m-.053.514c.18 0 .327.148.327.327v.888c0
 .179-.147.326-.327.326h-1.244c-.18
 0-.326-.147-.326-.326v-.888c0-.179.146-.327.326-.327zm.053
 1.213v-.884c0-.035-.029-.064-.064-.064h-1.222c-.035
 0-.064.029-.064.064v.884c0 .035.029.063.064.063h1.222c.035 0
 .064-.028.064-.063m5.128-.322c.296.117.921.212 1.408.212.534 0
 .755-.183.755-.413
 0-.207-.205-.328-.795-.544-.787-.292-1.365-.521-1.365-1.038
 0-.536.695-.851 1.755-.851.569 0 .765.036
 1.126.102l.003.508c-.355-.067-.67-.183-1.159-.183-.523
 0-.747.166-.747.337 0 .25.344.369.947.583.84.301 1.307.533 1.307 1.04
 0 .521-.585.897-1.904.897-.542
 0-.916-.036-1.331-.102zm-1.123.414c-.311.14-.898.229-1.412.229h-1.962v-3.27h1.962c.514
 0 1.101.09 1.413.231.755.341 1.002.887 1.002 1.405 0 .517-.245
 1.063-1.003 1.405m-1.685-2.599h-.629v2.377h.629c.963 0 1.571-.412
 1.571-1.183 0-.772-.608-1.194-1.571-1.194m6.4
 2.806h-.096v-.378h-.139v-.081h.374v.081h-.139zm.675
 0h-.089v-.384h-.001l-.086.384h-.094l-.084-.384h-.001v.384h-.089v-.459h.139l.083.361h.001l.082-.361H24z"
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
        return '''https://www.nintendo.com/en-gb/Support/Ninten
do-DS/Nintendo-DS-manual-and-additional-documents/Nintendo-DS-manual-a
nd-additional-documents/Nintendo-DS-manual-and-additional-documents-61'''

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
