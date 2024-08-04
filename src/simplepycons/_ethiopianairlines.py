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


class EthiopianAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ethiopianairlines"

    @property
    def original_file_name(self) -> "str":
        return "ethiopianairlines.svg"

    @property
    def title(self) -> "str":
        return "Ethiopian Airlines"

    @property
    def primary_color(self) -> "str":
        return "#648B1A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ethiopian Airlines</title>
     <path d="M18.308 11.603c2.39-1.456 4.239-2.53 4.966-4.355
 1.544-4.17.363-5.865-1.104-4.564C20.293 4.506 11.478 13.754.195
 20.257c-.172.098-.2.322.558.091 4.48-1.572 14.23-6.705
 17.555-8.745zm1.823-.333c.942-.586 1.976-.237.316 2.466-1.126
 1.662-1.905 2.63-4.92 3.544-2.075.785-9.768 3.024-15.157
 3.675-.401.033-.524-.114-.128-.246 5.135-1.306 17.984-8.21
 19.889-9.44zm-8.977 10.47c2.204-.072 3.862.242 5.725-1.73 1.95-2.02
 1.72-3.07.544-2.743-1.745.524-8.111 2.69-15.622
 3.735-.338.046-.256.226.14.25 5.018.474 6.911.51 9.213.488Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://corporate.ethiopianairlines.com/media'''

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