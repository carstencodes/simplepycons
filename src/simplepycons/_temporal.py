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


class TemporalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "temporal"

    @property
    def original_file_name(self) -> "str":
        return "temporal.svg"

    @property
    def title(self) -> "str":
        return "Temporal"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Temporal</title>
     <path d="M16.206 7.794C15.64 3.546 14.204 0 12 0 9.796 0 8.361
 3.546 7.794 7.794 3.546 8.36 0 9.796 0 12c0 2.204 3.546 3.639 7.794
 4.206C8.36 20.453 9.796 24 12 24c2.204 0 3.639-3.546
 4.206-7.794C20.454 15.64 24 14.204 24
 12c0-2.204-3.547-3.64-7.794-4.206Zm-8.55
 7.174c-4.069-.587-6.44-1.932-6.44-2.969 0-1.036 2.372-2.381
 6.44-2.969-.09.98-.137 1.98-.137 2.97 0 .99.047 1.99.137 2.968zM12
 1.215c1.036 0 2.381 2.372 2.969 6.44a32.718 32.718 0 0 0-5.938
 0c.587-4.068 1.932-6.44 2.969-6.44Zm4.344
 13.753c-.2.03-1.022.126-1.23.146-.02.209-.117 1.03-.145 1.23-.588
 4.068-1.933 6.44-2.97 6.44-1.036
 0-2.38-2.372-2.968-6.44-.03-.2-.126-1.022-.147-1.23a31.833 31.833 0 0
 1 0-6.23 31.813 31.813 0 0 1 7.46.146c4.068.587 6.442 1.933 6.442
 2.969-.001 1.036-2.374 2.382-6.442 2.97z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/temporalio/temporaldotio/b
lob/b6b5f3ed1fda818d5d6c07e27ec15d51a61f2267/public/images/icons/tempo'''

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
