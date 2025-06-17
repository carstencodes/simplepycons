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


class UniqloJaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uniqlo_ja"

    @property
    def original_file_name(self) -> "str":
        return "uniqlo_ja.svg"

    @property
    def title(self) -> "str":
        return "Uniqlo"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Uniqlo</title>
     <path d="M0 .01v23.98h24V.01ZM4.291 3.29h4.553l.006
 5.803h1.511v1.511h-6.82V9.094h3.783v-4.29H4.291zm10.11
 0h5.302v1.514H14.4zm-.762 5.807h6.816v1.511H13.64zM4.29
 13.385l6.072.002-1.513
 7.322H2.777l.305-1.516h4.553l.892-4.29H5.49l-.457 2.148H3.521Zm9.348
 0h6.816v7.324H13.64zm1.517 1.517v4.291h3.787v-4.29z" />
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


class UniqloIcon1(UniqloJaIcon):
    """UniqloIcon1 is an alternative implementation name for UniqloJaIcon. 
          It is deprecated and may be removed in future versions."""
    def __init__(self, *args, **kwargs) -> "None":
        import warnings
        warnings.warn("The usage of 'UniqloIcon1' is discouraged and may be removed in future major versions. Use 'UniqloJaIcon' instead.", DeprecationWarning)
        super().__init__(*args, **kwargs)

