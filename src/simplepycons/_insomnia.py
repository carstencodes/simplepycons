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


class InsomniaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "insomnia"

    @property
    def original_file_name(self) -> "str":
        return "insomnia.svg"

    @property
    def title(self) -> "str":
        return "Insomnia"

    @property
    def primary_color(self) -> "str":
        return "#4000BF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Insomnia</title>
     <path d="M12.1356 3.4577c4.7179 0 8.5424 3.8245 8.5424 8.5424 0
 4.7178-3.8245 8.5423-8.5424 8.5423-4.7178
 0-8.5423-3.8245-8.5423-8.5423
 0-1.153.2284-2.2527.6425-3.2562.6046.8233 1.5796 1.3579 2.6795 1.3579
 1.8347 0 3.322-1.4874 3.322-3.3221
 0-1.0999-.5345-2.0749-1.3579-2.6795 1.0036-.414 2.1032-.6425
 3.2562-.6425zM12 0C5.3726 0 0 5.3726 0 12s5.3726 12 12 12 12-5.3726
 12-12S18.6274 0 12 0Zm0 1.2203c5.9534 0 10.7797 4.8263 10.7797
 10.7797S17.9534 22.7797 12 22.7797 1.2203 17.9534 1.2203 12 6.0466
 1.2203 12 1.2203Z" />
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
