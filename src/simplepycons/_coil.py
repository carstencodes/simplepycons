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


class CoilIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coil"

    @property
    def original_file_name(self) -> "str":
        return "coil.svg"

    @property
    def title(self) -> "str":
        return "Coil"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coil</title>
     <path d="M12 0A12 12 0 000 12a12 12 0 0012 12 12 12 0 0012-12A12
 12 0 0012 0zm.465 5.814a4.56 4.56 0 012.756.83c1.215.886 1.465 1.856
 1.465 2.5a1.845 1.845 0 01-.086.6 2.77 2.77 0 01-2.305 1.906 5.675
 5.675 0 01-.654.055c-1 0-1.33-.41-1.33-.87 0-.624.6-1.364
 1.035-1.364a.28.28 0 01.154.045.76.76 0 00.375.093.265.265 0 00.11 0
 .55.55 0 00.515-.558c0-.55-.625-1.25-2-1.25a5.285 5.285 0
 00-1.55.244A4.12 4.12 0 008.685 9.8 4 4 0 008 12.05 3.945 3.945 0
 008.5 14a4.235 4.235 0 003.69 2.06h.24c2-.11 2.46-1.09
 2.906-1.28a1.53 1.53 0 01.299-.065c.325 0 .745.164 1.035.86a.73.73 0
 01.07.3c0 1.145-2.67 2.18-4.22 2.26h-.35A6.38 6.38 0 016.62 15a5.9
 5.9 0 01-.77-2.94 6.085 6.085 0 011.035-3.39 6.195 6.195 0
 013.385-2.5 7.295 7.295 0 012.195-.356z" />
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
