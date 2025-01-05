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


class VaadinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vaadin"

    @property
    def original_file_name(self) -> "str":
        return "vaadin.svg"

    @property
    def title(self) -> "str":
        return "Vaadin"

    @property
    def primary_color(self) -> "str":
        return "#00B4F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vaadin</title>
     <path d="M1.166.521C.506.521 0 1.055 0 1.715v1.97c0 2.316 1.054
 3.473 3.502 3.473h5.43c1.623 0 1.783.685 1.783 1.35 0
 .068.004.13.012.193a1.268 1.268 0 0 0
 2.531-.004c.007-.062.012-.121.012-.19 0-.664.16-1.349
 1.783-1.349h5.43C22.93 7.158 24 6.001 24
 3.686V1.715c0-.66-.524-1.194-1.184-1.194-.66 0-1.189.534-1.189
 1.194l-.004.685c0 .746-.476 1.27-1.594 1.27h-5.322c-2.422 0-2.608
 1.796-2.687 2.748h-.055c-.08-.952-.266-2.748-2.688-2.748H3.955c-1.118
 0-1.629-.544-1.629-1.29v-.665c0-.66-.5-1.194-1.16-1.194zm5.875
 10.553a1.586 1.586 0 0 0-1.375 2.371c1.657 3.06 3.308 6.13 4.967
 9.184a1.415 1.415 0 0 0 2.586.02l.033-.06 4.945-9.142a1.587 1.587 0 0
 0-1.377-2.373c-.702 0-1.179.345-1.502 1.082l-3.386
 6.313-3.383-6.305c-.326-.745-.805-1.09-1.508-1.09Z" />
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
